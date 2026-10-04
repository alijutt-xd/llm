from datetime import datetime, timedelta
from typing import Dict, List, Optional


class CatalogService:
    """Model catalog and sync service."""

    def __init__(self, db, provider_service, sync_interval_hours: int = 12):
        """Initialize catalog service."""
        self.db = db
        self.provider_service = provider_service
        self.sync_interval_hours = sync_interval_hours
        self.last_sync = None
        self.builtin_models = self._load_builtin_models()
        self.custom_models = {}

    def _load_builtin_models(self) -> Dict[str, dict]:
        """Load built-in models."""
        return {
            "gpt-4o": {"provider": "openai", "context_window": 128000},
            "gpt-4o-mini": {"provider": "openai", "context_window": 128000},
            "gpt-4-turbo": {"provider": "openai", "context_window": 128000},
            "gpt-3.5-turbo": {"provider": "openai", "context_window": 4096},
            "claude-3-5-sonnet": {"provider": "anthropic", "context_window": 200000},
            "claude-3-opus": {"provider": "anthropic", "context_window": 200000},
            "claude-3-sonnet": {"provider": "anthropic", "context_window": 200000},
            "gemini-2.0-flash": {"provider": "google", "context_window": 1000000},
            "gemini-1.5-pro": {"provider": "google", "context_window": 1000000},
            "llama-2-70b": {"provider": "groq", "context_window": 4096},
            "llama-3.1-70b": {"provider": "groq", "context_window": 8192},
            "mixtral-8x7b": {"provider": "groq", "context_window": 32000},
            "mistral-large": {"provider": "mistral", "context_window": 32000},
            "mistral-medium": {"provider": "mistral", "context_window": 32000},
            "mistral-small": {"provider": "mistral", "context_window": 32000},
        }

    def get_all_models(self) -> List[dict]:
        """Get all available models."""
        models = []
        for provider in self.provider_service.get_all_providers():
            for model_name in provider.models:
                models.append(
                    {
                        "id": model_name,
                        "object": "model",
                        "owned_by": provider.name,
                        "provider": provider.name,
                        "base_url": provider.base_url,
                    }
                )
        return models

    def should_sync(self) -> bool:
        """Check if catalog should sync."""
        if self.last_sync is None:
            return True
        return datetime.utcnow() - self.last_sync > timedelta(
            hours=self.sync_interval_hours
        )

    async def sync(self) -> None:
        """Sync catalog from remote source."""
        # In production, this would fetch from freellmapi.co
        # For now, it's a placeholder for the catalog update mechanism
        self.last_sync = datetime.utcnow()
