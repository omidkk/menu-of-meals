"""A class to return the health"""
import logging

from flask_restx import Namespace, Resource, cors

from app import db

health_ns = Namespace(
    "health",
    description="health related operations",
    decorators=[cors.crossdomain(origin="*")],
)

_log = logging.getLogger(__name__)

@health_ns.route("/")
class HealthCheck(Resource):
    """health api class"""

    @health_ns.doc("return a health check")
    def get(self):
         try:
            # to check database we will execute raw query
            db.session.execute("SELECT 1")
            return (
                {"Status": "Healthy", "DB Connection": "Available"},
                200,
                {"content-type": "application/json"},
            )
         except Exception:
            _log.warning({"Status": "Unhealthy", "DB Connection": "Unavailable"})
            return (
                {"Status": "Unhealthy", "DB Connection": "Unavailable"},
                500,
                {"content-type": "application/json"},
            )
