import json
from typing import Optional, Dict, Any
from llm.models import Provider


class ProviderService:
    """Provider management service."""

    def __init__(self, db):
        """Initialize provider service."""
        self.db = db
        self.providers: Dict[str, Provider] = {}
        self._load_default_providers()

    def _load_default_providers(self) -> None:
        """Load default provider configurations."""
        # This would be loaded from database in production
        pass

    def add_provider(self, provider: Provider) -> None:
        """Add or update provider."""
        self.providers[provider.name] = provider

    def get_provider(self, name: str) -> Optional[Provider]:
        """Get provider by name."""
        return self.providers.get(name)

    def get_providers_for_model(self, model_name: str) -> list:
        """Get all providers that support a model."""
        matching = [
            p for p in self.providers.values()
            if p.enabled and p.matches_model(model_name)
        ]
        return sorted(matching, key=lambda p: p.priority)

    def resolve_provider(
        self, model_name: str
    ) -> Optional[Provider]:
        """Resolve best provider for model."""
        candidates = self.get_providers_for_model(model_name)
        if not candidates:
            return None
        return candidates[0]

    def get_all_providers(self) -> list:
        """Get all providers."""
        return sorted(
            self.providers.values(),
            key=lambda p: p.priority,
        )

    def list_providers(self) -> list:
        """List all providers with metadata."""
        return [p.to_dict() for p in self.get_all_providers()]

    def delete_provider(self, name: str) -> bool:
        """Delete provider."""
        if name in self.providers:
            del self.providers[name]
            return True
        return False
