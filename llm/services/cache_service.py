import hashlib
import json
from datetime import datetime, timedelta
from typing import Optional, Dict, Any


class CacheService:
    """Response caching service."""

    def __init__(self, db, max_entries: int = 5000, ttl_seconds: int = 3600):
        """Initialize cache service."""
        self.db = db
        self.max_entries = max_entries
        self.ttl_seconds = ttl_seconds
        self.memory_cache: Dict[str, tuple] = {}  # (response, expiry_time)

    def _hash_request(
        self, model: str, messages: list, **kwargs
    ) -> str:
        """Generate cache key from request."""
        request_data = {
            "model": model,
            "messages": messages,
            **kwargs,
        }
        request_json = json.dumps(request_data, sort_keys=True)
        return hashlib.sha256(request_json.encode()).hexdigest()

    def get(
        self,
        model: str,
        messages: list,
        **kwargs
    ) -> Optional[Dict[str, Any]]:
        """Get cached response if available."""
        cache_key = self._hash_request(model, messages, **kwargs)
        now = datetime.utcnow()

        # Check memory cache first
        if cache_key in self.memory_cache:
            response, expiry = self.memory_cache[cache_key]
            if now < expiry:
                return response
            else:
                del self.memory_cache[cache_key]

        return None

    def set(
        self,
        model: str,
        messages: list,
        response: Dict[str, Any],
        **kwargs
    ) -> None:
        """Cache response."""
        cache_key = self._hash_request(model, messages, **kwargs)
        expiry = datetime.utcnow() + timedelta(seconds=self.ttl_seconds)
        self.memory_cache[cache_key] = (response, expiry)

        # Evict LRU if cache is full
        if len(self.memory_cache) > self.max_entries:
            oldest_key = min(
                self.memory_cache.keys(),
                key=lambda k: self.memory_cache[k][1],
            )
            del self.memory_cache[oldest_key]

    def clear(self) -> None:
        """Clear cache."""
        self.memory_cache.clear()
