from flask import Flask
from flask_cors import CORS

from .config import Config
from .extensions import register_extensions
from .routes.api import api_bp
from .routes.admin import admin_bp
from .services.provider_manager import ProviderManager


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    CORS(app, resources={r"/v1/*": {"origins": "*"}})
    register_extensions(app)

    app.provider_manager = ProviderManager(
        config_path=app.config["PROVIDERS_CONFIG_PATH"],
        secret_key=app.config["SECRET_KEY"],
    )
    app.provider_manager.load()

    app.register_blueprint(api_bp)
    app.register_blueprint(admin_bp)

    @app.get("/")
    def index():
        return {
            "project": "llm",
            "author": "ALi Jutt",
            "status": "running",
            "docs": "/v1/models",
        }

    return app
