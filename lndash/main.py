import sys

if sys.version_info.major != 3:
    raise OSError("Python 3 is required")

import logging
import filters
import views
from cache import cache
from flask import Flask

app = Flask(__name__)
app.register_blueprint(filters.blueprint)
app.register_blueprint(views.blueprint)
gunicorn_logger = logging.getLogger('gunicorn.error')
app.logger.handlers = gunicorn_logger.handlers

cache.init_app(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
