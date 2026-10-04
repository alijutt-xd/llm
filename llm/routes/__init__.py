"""Routes module."""

from flask import Blueprint

api_bp = Blueprint("api", __name__, url_prefix="/v1")
admin_bp = Blueprint("admin", __name__, url_prefix="/admin")
auth_bp = Blueprint("auth", __name__, url_prefix="/auth")
