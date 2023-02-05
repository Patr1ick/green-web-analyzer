from flask import Flask
from flask.logging import default_handler
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from logging.config import dictConfig
import logging

from .views import setupRoutes


def create_app(app_name="greenwebanalyzer"):

    dictConfig({
        'version': 1,
        'formatters': {
            'default': {
                'format': '%(asctime)s [%(levelname)s] %(message)s'
            },
        },
        'handlers': {
            'wsgi': {
                'formatter': 'default',
                'class': 'logging.StreamHandler',
                'stream': 'ext://flask.logging.wsgi_errors_stream',
            },
        },
        'root': {
            'level': 'INFO',
            'handlers': ['wsgi']
        }
    })

    log = logging.getLogger('werkzeug')
    log.disabled = True

    app = Flask(
        app_name
    )

    app.logger.removeHandler(default_handler)

    limiter = Limiter(
        get_remote_address,
        app=app,
        default_limits=['100 per hour'],
    )

    setupRoutes(app, limiter)

    return app
