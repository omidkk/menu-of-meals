"""A class to return the meny"""
import logging
from datetime import datetime

from flask_restx import Namespace, Resource, cors

menu_ns = Namespace("menu", description="meny related operations", decorators=[cors.crossdomain(origin="*")],)

_log = logging.getLogger(__name__)


@menu_ns.route("/<string:date>/<string:type>")
class HealthCheck(Resource):
    """menu api class"""

    @menu_ns.doc("return a menu of day")
    def get(self, date:str, meal_type: str):
        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            _log.error(f"Incorrect data format {date}, should be YYYY-MM-DD")
            return f"Incorrect data format {date}, should be YYYY-MM-DD", 500

        return "HIIII", 200
