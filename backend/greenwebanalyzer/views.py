from json import JSONDecodeError
import os

from flask import request, abort, json, jsonify, make_response, Response
from werkzeug.exceptions import HTTPException

import validators

# Time
from datetime import datetime
import pytz

from .report import Report

# Error
from selenium.common.exceptions import WebDriverException


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

    @app.route('/health', methods=['GET'])
    def health():
        return {}, 200

    @app.route('/request', methods=['POST', 'OPTIONS'])
    @limiter.limit("10/minute")
    def request_report():
        if request.method == 'OPTIONS':
            return _build_cors_preflight()

        request_data = request.get_json()

        # Check if no URL was given or
        try:
            if request_data['url'] == None:
                abort(400, description="No URL was provided.")
        except KeyError:
            abort(400, description="Wrong payload was provided.")

        url = request_data['url']

        # Check if URL is valid
        if not validators.url(url):
            app.logger.error("Invalid URL was given: %s", url)
            abort(400, description="Provided URL is not valid.")

        r = Report(url, app=app)
        try:
            report = r.create_report()
        except WebDriverException:
            abort(500, description="Failed to retrieve website.")

        response = make_response(jsonify(report), 201)
        return response

    @app.after_request
    def after_request(response: Response):
        if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
            ip = request.remote_addr
        else:
            ip = request.headers['X-Forwarded-For']

        app.logger.info({
            "date:": datetime.now(pytz.timezone('Europe/Berlin')).strftime('%Y-%m-%dT%H:%M:%S:%f%z'),
            "path": request.path,
            "method": request.method,
            "ip": ip,
            "user_agent": request.headers.get('User-Agent'),
            "status": response.status,
            "content_length": response.content_length,
            "data": response.get_data(as_text=True)
        })

        if os.getenv('APP_ENVIRONMENT') == "local" or os.getenv('APP_ENVIRONMENT') == "debug":
            response.headers.add(
                "Access-Control-Allow-Origin",
                "*"
            )
            response.headers.add('Access-Control-Allow-Headers', "*")
            response.headers.add('Access-Control-Allow-Methods', "*")
        else:
            response.headers.add(
                "Access-Control-Allow-Origin",
                "https://green-web-analyzer.eu"
            )
            response.headers.add('Access-Control-Allow-Headers', "Content-Type")
            response.headers.add('Access-Control-Allow-Methods', "POST")

        return response


def _build_cors_preflight():
    response = make_response()
    return response
