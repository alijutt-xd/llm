import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")


class Config:
    """Application configuration."""

    # App info
    APP_NAME = os.getenv("APP_NAME", "llm")
    APP_AUTHOR = os.getenv("APP_AUTHOR", "Ali Jutt")
    APP_VERSION = "0.1.0"

    # Flask
    FLASK_ENV = os.getenv("FLASK_ENV", "development")
    DEBUG = FLASK_ENV == "development"
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key-change-in-production")
    JSON_SORT_KEYS = False

    # Server
    PORT = int(os.getenv("PORT", 5000))
    HOST = os.getenv("HOST", "::")

    # Database
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", f"sqlite:///{BASE_DIR / 'llm.db'}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Encryption
    ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY", "change-me-in-production")

    # Rate limiting
    PROXY_RATE_LIMIT_RPM = int(os.getenv("PROXY_RATE_LIMIT_RPM", 120))
    ADMIN_RATE_LIMIT_RPM = int(os.getenv("ADMIN_RATE_LIMIT_RPM", 600))
    REQUEST_BODY_LIMIT_MB = int(os.getenv("REQUEST_BODY_LIMIT_MB", 25))

    # Timeouts (milliseconds)
    PROVIDER_TIMEOUT_DEFAULT = int(os.getenv("PROVIDER_TIMEOUT_DEFAULT", 60000))
    PROVIDER_STREAM_STALL_TIMEOUT_MS = int(
        os.getenv("PROVIDER_STREAM_STALL_TIMEOUT_MS", 90000)
    )
    FALLBACK_TIME_BUDGET_MS = int(os.getenv("FALLBACK_TIME_BUDGET_MS", 45000))

    # Cache
    RESPONSE_CACHE = os.getenv("RESPONSE_CACHE", "false").lower() == "true"
    RESPONSE_CACHE_PERSIST = os.getenv("RESPONSE_CACHE_PERSIST", "true").lower() == "true"
    RESPONSE_CACHE_TTL_SECONDS = int(os.getenv("RESPONSE_CACHE_TTL_SECONDS", 3600))
    RESPONSE_CACHE_MAX_TEMPERATURE = float(
        os.getenv("RESPONSE_CACHE_MAX_TEMPERATURE", 1.0)
    )
    RESPONSE_CACHE_MAX_ENTRIES = int(
        os.getenv("RESPONSE_CACHE_MAX_ENTRIES", 5000)
    )

    # Analytics
    REQUEST_ANALYTICS_RETENTION_DAYS = int(
        os.getenv("REQUEST_ANALYTICS_RETENTION_DAYS", 90)
    )
    REQUEST_ANALYTICS_MAX_ROWS = int(
        os.getenv("REQUEST_ANALYTICS_MAX_ROWS", 100000)
    )
    REQUEST_ANALYTICS_LOG_CLIENT = (
        os.getenv("REQUEST_ANALYTICS_LOG_CLIENT", "true").lower() == "true"
    )

    # Compression
    FREELLMAPI_COMPRESSION = os.getenv("FREELLMAPI_COMPRESSION", "off")

    # Proxy
    PROXY_URL = os.getenv("PROXY_URL", "")
    NO_PROXY = os.getenv("NO_PROXY", "localhost,127.0.0.1")
    FREEAPI_PROXY_LOCAL_DESTINATIONS = (
        os.getenv("FREEAPI_PROXY_LOCAL_DESTINATIONS", "false").lower() == "true"
    )
    FREEAPI_BLOCK_PRIVATE_PROVIDER_URLS = (
        os.getenv("FREEAPI_BLOCK_PRIVATE_PROVIDER_URLS", "false").lower() == "true"
    )

    # Features
    FREELLMAPI_CONTEXT_HANDOFF = os.getenv(
        "FREELLMAPI_CONTEXT_HANDOFF", "on_model_switch"
    )
    VALIDATE_TOOL_ARGUMENTS = (
        os.getenv("VALIDATE_TOOL_ARGUMENTS", "false").lower() == "true"
    )
    FALLBACK_DETAIL_HEADER = (
        os.getenv("FALLBACK_DETAIL_HEADER", "false").lower() == "true"
    )

    # Dashboard
    DASHBOARD_ORIGINS = os.getenv(
        "DASHBOARD_ORIGINS",
        "localhost:5173,127.0.0.1:5173,[::1]:5173",
    )

    # Update checker
    FREELLMAPI_UPDATE_CHECK = (
        os.getenv("FREELLMAPI_UPDATE_CHECK", "off").lower() != "off"
    )
