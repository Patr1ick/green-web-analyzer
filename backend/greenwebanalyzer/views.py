import os

def setupRoutes(app):

    @app.route('/version')
    def version():
        return {
            "environment": os.getenv('APP_ENVIRONMENT'),
            "version": os.getenv('APP_VERSION')
        }