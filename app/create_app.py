"""Initialize Flask app."""
import logging

from app import db
from config import Config
from flask import Flask
from rest.api import api_v1

_log = logging.getLogger(__name__)


def create_app():
    """Construct the core application."""
    _log.info("start create the app.")

    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(api_v1)

    return app
