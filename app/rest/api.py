"""A class to import all apis"""

import logging

from flask import Blueprint
from flask_restx import Api

from app.rest.v1.health_rest import health_ns
from app.rest.v1.menu_rest import menu_ns

_log = logging.getLogger(__name__)

api_v1 = Blueprint("api_v1", __name__, url_prefix="/v1")
api = Api(api_v1, doc="/docs", version="1.0", title="Menu of Meals")


api.add_namespace(health_ns)
api.add_namespace(menu_ns)
