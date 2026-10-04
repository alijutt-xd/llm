import requests


class FailoverManager:
    def __init__(self, provider_manager):
        self.provider_manager = provider_manager

    def call_with_fallback(self, model_name: str, operation: str, payload: dict):
        candidates = self.provider_manager.get_providers_for_model(model_name)
        if not candidates:
            raise ValueError(f"No provider available for model: {model_name}")

        last_error = None
        for provider in candidates:
            try:
                return self._invoke(provider, operation, payload)
            except Exception as exc:
                last_error = exc
                continue

        if last_error:
            raise last_error
        raise RuntimeError(f"Provider call failed for model: {model_name}")

    def _invoke(self, provider, operation: str, payload: dict):
        endpoint = self._build_endpoint(provider, operation)
        response = requests.post(
            endpoint,
            headers=provider.headers(),
            json=payload,
            timeout=provider.timeout,
        )

        if response.status_code >= 400:
            raise RuntimeError(
                f"{provider.name} returned status {response.status_code}: {response.text}"
            )

        try:
            return response.json()
        except ValueError:
            return {"raw_response": response.text}

    def _build_endpoint(self, provider, operation: str):
        base = provider.base_url.rstrip("/")
        if base.endswith("/v1"):
            return f"{base}/{operation}"
        return f"{base}/v1/{operation}"
