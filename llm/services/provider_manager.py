import json
from pathlib import Path

from llm.models import ProviderConfig
from llm.services.crypto import SecretManager


class ProviderManager:
    def __init__(self, config_path: str, secret_key: str):
        self.config_path = Path(config_path)
        self.secret_manager = SecretManager(secret_key)
        self.providers = []

    def _ensure_parent_dir(self):
        self.config_path.parent.mkdir(parents=True, exist_ok=True)

    def _default_config(self):
        return {
            "providers": [
                {
                    "name": "demo-openai-compatible",
                    "base_url": "https://api.openai.com/v1",
                    "api_key": "replace_me",
                    "enabled": False,
                    "models": ["gpt-4o-mini", "gpt-4o", "gpt-3.5-turbo"],
                    "priority": 1,
                    "provider_type": "openai-compatible",
                    "timeout": 30,
                }
            ]
        }

    def load(self):
        self._ensure_parent_dir()

        if not self.config_path.exists():
            self.config_path.write_text(
                json.dumps(self._default_config(), indent=2),
                encoding="utf-8",
            )

        raw = self.config_path.read_text(encoding="utf-8")
        data = json.loads(raw or "{}")

        providers = data.get("providers", [])
        self.providers = []

        for provider in providers:
            api_key = provider.get("api_key", "")
            if api_key.startswith("enc:"):
                try:
                    api_key = self.secret_manager.decrypt(api_key)
                except Exception:
                    api_key = ""

            cfg = ProviderConfig(
                name=provider.get("name", "unnamed"),
                base_url=provider.get("base_url", ""),
                api_key=api_key,
                enabled=provider.get("enabled", True),
                models=provider.get("models", []),
                priority=provider.get("priority", 100),
                timeout=provider.get("timeout", 30),
                provider_type=provider.get("provider_type", "openai-compatible"),
            )
            if cfg.enabled:
                self.providers.append(cfg)

        self.providers = sorted(self.providers, key=lambda p: p.priority)

    def save(self):
        self._ensure_parent_dir()

        payload = {"providers": []}
        for provider in self.providers:
            encrypted_key = provider.api_key
            if provider.api_key:
                encrypted_key = "enc:" + self.secret_manager.encrypt(provider.api_key)

            payload["providers"].append(
                {
                    "name": provider.name,
                    "base_url": provider.base_url,
                    "api_key": encrypted_key,
                    "enabled": provider.enabled,
                    "models": provider.models,
                    "priority": provider.priority,
                    "timeout": provider.timeout,
                    "provider_type": provider.provider_type,
                }
            )

        self.config_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    def add_provider(self, provider_config: ProviderConfig):
        existing = next((p for p in self.providers if p.name == provider_config.name), None)
        if existing:
            self.providers.remove(existing)
        self.providers.append(provider_config)
        self.providers = sorted(self.providers, key=lambda p: p.priority)
        self.save()

    def get_providers_for_model(self, model_name: str):
        matches = [p for p in self.providers if p.enabled and p.matches(model_name)]
        return sorted(matches, key=lambda p: p.priority)

    def resolve_provider(self, model_name: str):
        candidates = self.get_providers_for_model(model_name)
        if not candidates:
            return None
        return candidates[0]

    def list_models(self):
        models = []
        for provider in self.providers:
            for model in provider.models:
                models.append(
                    {
                        "id": model,
                        "object": "model",
                        "owned_by": provider.name,
                        "provider": provider.name,
                        "base_url": provider.base_url,
                    }
                )
        return models

    def get_all_providers(self):
        return self.providers
