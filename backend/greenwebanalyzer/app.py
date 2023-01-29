from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from .views import setupRoutes


def create_app(app_name="greenwebanalyzer"):
    app = Flask(
        app_name
    )
    limiter = Limiter(
        get_remote_address,
        app=app,
        default_limits=['100 per hour'],
    )

    setupRoutes(app, limiter)

    return app
