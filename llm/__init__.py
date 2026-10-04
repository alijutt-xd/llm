from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from llm.config import Config
from llm.extensions import db, init_extensions
from llm.routes import api_bp, admin_bp, auth_bp
from llm.services.provider_service import ProviderService
from llm.services.catalog_service import CatalogService
from llm.services.health_service import HealthService
from llm.services.cache_service import CacheService
from llm.lib.scheduler import Scheduler


def create_app(config_class=Config):
    """Application factory."""
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config.from_object(config_class)
    app.secret_key = config_class.SECRET_KEY

    # Initialize extensions
    init_extensions(app)

    # CORS setup
    CORS(
        app,
        resources={
            r"/v1/*": {"origins": "*"},
            r"/v1beta/*": {"origins": "*"},
            r"/mcp/*": {"origins": "*"},
        },
    )

    # Initialize core services
    app.provider_service = ProviderService(db)
    app.catalog_service = CatalogService(db, app.provider_service)
    app.health_service = HealthService(app.provider_service, db)
    app.cache_service = CacheService(db) if app.config.get("RESPONSE_CACHE") else None
    app.scheduler = Scheduler()

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(api_bp)
    app.register_blueprint(admin_bp)

    # Health check endpoint
    @app.get("/")
    def index():
        return {
            "project": "llm",
            "author": "Ali Jutt",
            "status": "running",
            "version": "0.1.0",
            "docs": "/v1/models",
        }

    @app.get("/health")
    def health():
        return {"status": "ok", "service": "llm-gateway"}

    with app.app_context():
        db.create_all()

    return app
