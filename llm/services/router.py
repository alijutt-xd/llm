class ModelRouter:
    def __init__(self, provider_manager):
        self.provider_manager = provider_manager

    def resolve(self, model_name: str):
        candidates = self.provider_manager.get_providers_for_model(model_name)
        if not candidates:
            return None
        return candidates[0]

    def get_fallback_chain(self, model_name: str):
        candidates = self.provider_manager.get_providers_for_model(model_name)
        if not candidates:
            return []
        return [provider.name for provider in candidates]
