"""A class to return the meny"""
import logging
from datetime import datetime

from flask_restx import Namespace, Resource, cors

from app.services.menu_service import MenuService

menu_ns = Namespace(
    "menu",
    description="meny related operations",
    decorators=[cors.crossdomain(origin="*")],
)

_log = logging.getLogger(__name__)


@menu_ns.route("/<string:date>/<string:meal_type>")
class HealthCheck(Resource):
    """menu api class"""

    @menu_ns.doc("return a menu of day")
    def get(self, date: str, meal_type: str):
        try:
            date = datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            _log.error("Incorrect data format  %s, should be YYYY-MM-DD and valid date.", date)
            return f"Incorrect data format {date}, should be YYYY-MM-DD and valid date.", 500

        meel_menu = MenuService.get_date_menu(meal_type, date)
        if meel_menu:
            return meel_menu, 200, {"content-type": "application/json"}
        return "", 204, {"content-type": "application/json"}
