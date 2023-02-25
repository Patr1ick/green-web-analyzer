from greenwebanalyzer import create_app

import os

app = create_app()

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        debug=(os.getenv('APP_ENVIRONMENT') == 'debug')
    )
