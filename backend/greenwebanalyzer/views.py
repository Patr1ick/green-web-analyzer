import os

from flask import request, abort, json
from werkzeug.exceptions import HTTPException

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

    @ app.route('/version')
    def version():
        return {
            "environment": os.getenv('APP_ENVIRONMENT'),
            "version": os.getenv('APP_VERSION')
        }, 200

    @app.route('/request', methods=['POST'])
    @limiter.limit("10 per hour")
    def request_report():
        request_data = request.get_json()

        # Check if no URL was given or
        try:
            if request_data['url'] == None:
                abort(400, description="No URL given.")
        except KeyError:
            abort(400, description="Bad Request")

        url = request_data['url']

        report = Report(url).create_report()

        return report, 201
