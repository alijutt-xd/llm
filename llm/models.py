from dataclasses import dataclass, field
from typing import List


@dataclass
class ProviderConfig:
    name: str
    base_url: str
    api_key: str = ""
    enabled: bool = True
    models: List[str] = field(default_factory=list)
    priority: int = 100
    timeout: int = 30
    provider_type: str = "openai-compatible"

    def matches(self, model_name: str) -> bool:
        normalized = model_name.lower()
        for model in self.models:
            if model.lower() == normalized:
                return True
        for model in self.models:
            if normalized.startswith(model.lower()):
                return True
        return False

    def headers(self):
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        return headers
