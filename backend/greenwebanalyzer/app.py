from flask import Flask

from .views import setupRoutes

def create_app(app_name="greenwebanalyzer"):
    app = Flask(
        app_name
    )

    setupRoutes(app)

    return app