from flask import Blueprint, current_app, jsonify, request
from llm.models import Provider, ProviderType

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


@admin_bp.route("/providers", methods=["GET"])
def list_providers():
    """List all providers."""
    providers = current_app.provider_service.list_providers()
    return jsonify({"providers": providers})


@admin_bp.route("/providers", methods=["POST"])
def add_provider():
    """Add new provider."""
    payload = request.get_json(silent=True) or {}

    # Validate required fields
    if not payload.get("name") or not payload.get("base_url"):
        return jsonify(
            {"error": "name and base_url are required"}
        ), 400

    try:
        provider = Provider(
            name=payload["name"],
            provider_type=ProviderType(payload.get("provider_type", "openai-compatible")),
            base_url=payload["base_url"],
            api_key=payload.get("api_key", ""),
            enabled=payload.get("enabled", True),
            models=payload.get("models", []),
            priority=payload.get("priority", 100),
            timeout_ms=payload.get("timeout_ms", 60000),
        )
        current_app.provider_service.add_provider(provider)
        return jsonify({"status": "ok", "provider": provider.name}), 201
    except Exception as exc:
        return jsonify({"error": str(exc)}), 400


@admin_bp.route("/providers/<name>", methods=["DELETE"])
def delete_provider(name):
    """Delete provider."""
    if current_app.provider_service.delete_provider(name):
        return jsonify({"status": "deleted", "provider": name})
    else:
        return jsonify({"error": f"Provider '{name}' not found"}), 404


@admin_bp.route("/providers/<name>", methods=["PUT"])
def update_provider(name):
    """Update provider."""
    payload = request.get_json(silent=True) or {}
    provider = current_app.provider_service.get_provider(name)

    if not provider:
        return jsonify({"error": f"Provider '{name}' not found"}), 404

    # Update fields
    for field in ["enabled", "priority", "timeout_ms", "models"]:
        if field in payload:
            setattr(provider, field, payload[field])

    return jsonify({"status": "ok", "provider": provider.to_dict()})


@admin_bp.route("/stats", methods=["GET"])
def stats():
    """Get gateway statistics."""
    providers = current_app.provider_service.get_all_providers()
    return jsonify(
        {
            "providers_count": len(providers),
            "enabled_providers": sum(1 for p in providers if p.enabled),
            "models_count": sum(len(p.models) for p in providers),
            "uptime_ms": 0,  # Would be tracked by scheduler
        }
    )
