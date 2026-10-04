from flask import Blueprint, current_app, jsonify, request

from llm.models import ProviderConfig

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


@admin_bp.route("/providers", methods=["GET"])
def list_providers():
    return jsonify(
        {
            "providers": [
                {
                    "name": provider.name,
                    "base_url": provider.base_url,
                    "enabled": provider.enabled,
                    "models": provider.models,
                    "priority": provider.priority,
                    "timeout": provider.timeout,
                    "provider_type": provider.provider_type,
                }
                for provider in current_app.provider_manager.get_all_providers()
            ]
        }
    )


@admin_bp.route("/providers", methods=["POST"])
def add_provider():
    payload = request.get_json(silent=True) or {}
    provider = ProviderConfig(
        name=payload.get("name"),
        base_url=payload.get("base_url", ""),
        api_key=payload.get("api_key", ""),
        enabled=payload.get("enabled", True),
        models=payload.get("models", []),
        priority=payload.get("priority", 100),
        timeout=payload.get("timeout", 30),
        provider_type=payload.get("provider_type", "openai-compatible"),
    )

    if not provider.name or not provider.base_url:
        return jsonify({"error": "name and base_url are required"}), 400

    current_app.provider_manager.add_provider(provider)
    return jsonify({"status": "ok", "provider": provider.name}), 201


@admin_bp.route("/providers/<name>", methods=["DELETE"])
def delete_provider(name):
    remaining = [provider for provider in current_app.provider_manager.get_all_providers() if provider.name != name]
    current_app.provider_manager.providers = remaining
    current_app.provider_manager.save()
    return jsonify({"status": "deleted", "provider": name})
