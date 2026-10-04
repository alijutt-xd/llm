from datetime import datetime
from typing import Dict, Optional


class HealthService:
    """Provider health checking service."""

    def __init__(self, provider_service, db):
        """Initialize health service."""
        self.provider_service = provider_service
        self.db = db
        self.health_status: Dict[str, dict] = {}

    async def check_provider_health(self, provider_name: str) -> bool:
        """Check if provider is healthy."""
        provider = self.provider_service.get_provider(provider_name)
        if not provider:
            return False

        # Implement actual health check logic here
        # For now, always return healthy
        provider.health_status = "healthy"
        provider.last_health_check = datetime.utcnow()
        return True

    async def check_all_providers(self) -> Dict[str, bool]:
        """Check health of all providers."""
        results = {}
        for provider in self.provider_service.get_all_providers():
            results[provider.name] = await self.check_provider_health(
                provider.name
            )
        return results

    def get_health_status(self, provider_name: str) -> Optional[dict]:
        """Get provider health status."""
        provider = self.provider_service.get_provider(provider_name)
        if not provider:
            return None
        return {
            "provider": provider.name,
            "status": provider.health_status,
            "last_check": provider.last_health_check,
        }
