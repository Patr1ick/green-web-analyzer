import os

from flask import request, abort, json, jsonify, make_response
from werkzeug.exceptions import HTTPException

import validators

from .report import Report


def setupRoutes(app, limiter):

    @app.errorhandler(HTTPException)
    def handle_error(e):
        response = e.get_response()
        response.data = json.dumps({
            "code": e.code,
            "name": e.name,
            "description": e.description,
        })
        response.content_type = "application/json"
        return response

    @app.route('/version')
    def version():
        return {
            "environment": os.getenv('APP_ENVIRONMENT'),
            "version": os.getenv('APP_VERSION')
        }, 200

    @app.route('/request', methods=['POST', 'OPTIONS'])
    @limiter.limit("10 per hour")
    def request_report():
        if request.method == 'OPTIONS':
            return _build_cors_preflight()

        request_data = request.get_json()

        # Check if no URL was given or
        try:
            if request_data['url'] == None:
                abort(400, description="No URL given.")
        except KeyError:
            abort(400, description="Bad Request")

        url = request_data['url']

        # Check if URL is valid
        if not validators.url(url):
            app.logger.error("Invalid URL was given: %s", url)
            abort(400, description="No valid URL given.")

        r = Report(url)
        report = r.create_report()

        app.logger.info({
            "date:": r.date.strftime('%Y-%m-%dT%H:%M:%S:%f%z'),
            "ip": request.remote_addr,
            "user_agent": request.headers.get('User-Agent'),
            "url": url,
            "response": 201
        })

        response = make_response(jsonify(report), 201)
        response.headers.add(
            "Access-Control-Allow-Origin",
            "https://green-web-analyzer.eu"
        )
        return response


def _build_cors_preflight():
    response = make_response()
    response.headers.add(
        "Access-Control-Allow-Origin",
        "https://green-web-analyzer.eu"
    )
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response
