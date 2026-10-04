import requests
from flask import Blueprint, current_app, jsonify, request

api_bp = Blueprint("api", __name__, url_prefix="/v1")


@api_bp.route("/health", methods=["GET"])
def health():
    return jsonify(
        {
            "status": "ok",
            "app": "llm",
            "author": "ALi Jutt",
            "providers_count": len(current_app.provider_manager.get_all_providers()),
        }
    )


@api_bp.route("/models", methods=["GET"])
def list_models():
    return jsonify({"object": "list", "data": current_app.provider_manager.list_models()})


@api_bp.route("/chat/completions", methods=["POST"])
def chat_completions():
    data = request.get_json(silent=True) or {}
    model = data.get("model", current_app.config.get("DEFAULT_MODEL", "gpt-4o-mini"))
    messages = data.get("messages", [])

    provider = current_app.provider_manager.resolve_provider(model)
    if not provider:
        return jsonify({"error": f"Model '{model}' is not available"}), 404

    payload = {"model": model, "messages": messages}
    payload.update({k: v for k, v in data.items() if k not in {"model", "messages"}})

    try:
        response = requests_post_compatible(provider, "chat/completions", payload)
        return jsonify(response)
    except Exception as exc:
        return jsonify({"error": str(exc)}), 502


@api_bp.route("/completions", methods=["POST"])
def completions():
    data = request.get_json(silent=True) or {}
    model = data.get("model", current_app.config.get("DEFAULT_MODEL", "gpt-4o-mini"))
    prompt = data.get("prompt", "")

    provider = current_app.provider_manager.resolve_provider(model)
    if not provider:
        return jsonify({"error": f"Model '{model}' is not available"}), 404

    payload = {"model": model, "prompt": prompt}
    payload.update({k: v for k, v in data.items() if k not in {"model", "prompt"}})

    try:
        response = requests_post_compatible(provider, "completions", payload)
        return jsonify(response)
    except Exception as exc:
        return jsonify({"error": str(exc)}), 502


@api_bp.route("/embeddings", methods=["POST"])
def embeddings():
    data = request.get_json(silent=True) or {}
    model = data.get("model", current_app.config.get("DEFAULT_MODEL", "gpt-4o-mini"))
    input_value = data.get("input", [])

    provider = current_app.provider_manager.resolve_provider(model)
    if not provider:
        return jsonify({"error": f"Model '{model}' is not available"}), 404

    payload = {"model": model, "input": input_value}
    payload.update({k: v for k, v in data.items() if k not in {"model", "input"}})

    try:
        response = requests_post_compatible(provider, "embeddings", payload)
        return jsonify(response)
    except Exception as exc:
        return jsonify({"error": str(exc)}), 502


def requests_post_compatible(provider, route_name: str, payload: dict):
    base = provider.base_url.rstrip("/")
    url = f"{base}/v1/{route_name}" if not base.endswith("/v1") else f"{base}/{route_name}"

    response = requests.post(
        url,
        headers=provider.headers(),
        json=payload,
        timeout=provider.timeout,
    )

    if response.status_code >= 400:
        raise RuntimeError(f"{provider.name} request failed: {response.status_code} - {response.text}")

    try:
        return response.json()
    except ValueError:
        return {"raw_response": response.text}
