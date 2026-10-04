from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any
from enum import Enum
import json


class ProviderType(str, Enum):
    """Provider type enumeration."""

    OPENAI_COMPATIBLE = "openai-compatible"
    ANTHROPIC = "anthropic"
    GOOGLE = "google"
    GROQ = "groq"
    MISTRAL = "mistral"
    OPENROUTER = "openrouter"
    COHERE = "cohere"
    OLLAMA = "ollama"
    CUSTOM = "custom"


class ModelType(str, Enum):
    """Model type enumeration."""

    CHAT = "chat"
    COMPLETION = "completion"
    EMBEDDING = "embedding"
    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"
    VISION = "vision"


@dataclass
class Provider:
    """Provider configuration."""

    name: str
    provider_type: ProviderType
    base_url: str
    api_key: str = ""
    api_key_header: str = "Authorization"
    api_key_prefix: str = "Bearer"
    enabled: bool = True
    priority: int = 100
    timeout_ms: int = 60000
    rate_limit_rpm: int = 60
    rate_limit_tpm: int = 100000
    models: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    health_status: str = "unknown"
    last_health_check: Optional[float] = None

    def get_auth_header(self) -> Optional[tuple]:
        """Get authorization header tuple."""
        if not self.api_key:
            return None
        header_value = (
            f"{self.api_key_prefix} {self.api_key}"
            if self.api_key_prefix
            else self.api_key
        )
        return (self.api_key_header, header_value)

    def matches_model(self, model_name: str) -> bool:
        """Check if provider supports model."""
        normalized = model_name.lower()
        for model in self.models:
            if model.lower() == normalized:
                return True
            if normalized.startswith(model.lower()):
                return True
        return False

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "name": self.name,
            "provider_type": self.provider_type.value,
            "base_url": self.base_url,
            "enabled": self.enabled,
            "priority": self.priority,
            "timeout_ms": self.timeout_ms,
            "rate_limit_rpm": self.rate_limit_rpm,
            "rate_limit_tpm": self.rate_limit_tpm,
            "models": self.models,
            "health_status": self.health_status,
        }


@dataclass
class Model:
    """Model configuration."""

    id: str
    name: str
    model_type: ModelType
    provider_name: str
    context_window: int = 4096
    max_tokens: int = 2048
    enabled: bool = True
    cost_per_1k_input: Optional[float] = None
    cost_per_1k_output: Optional[float] = None
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "id": self.id,
            "object": "model",
            "owned_by": self.provider_name,
            "name": self.name,
            "type": self.model_type.value,
            "context_window": self.context_window,
            "max_tokens": self.max_tokens,
        }
