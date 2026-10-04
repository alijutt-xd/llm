"""Routes package exports.

This file must re-export the actual blueprint instances from the route modules.
A common Flask bug is to define separate Blueprint objects in __init__.py and
then never register the real route blueprints from admin.py / api.py / auth.py.
"""

from .admin import admin_bp
from .api import api_bp
from .auth import auth_bp

__all__ = ["api_bp", "admin_bp", "auth_bp"]
