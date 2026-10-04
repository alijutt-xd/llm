import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")


class Config:
    APP_NAME = os.getenv("APP_NAME", "llm")
    APP_AUTHOR = os.getenv("APP_AUTHOR", "ALi Jutt")
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
    FLASK_ENV = os.getenv("FLASK_ENV", "development")
    PROVIDERS_CONFIG_PATH = os.getenv(
        "PROVIDERS_CONFIG_PATH",
        str(BASE_DIR / "data" / "providers.json"),
    )
    DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "gpt-4o-mini")
