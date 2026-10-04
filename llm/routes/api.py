import json
from flask import Blueprint, current_app, jsonify, request, Response
import httpx
import asyncio
from typing import AsyncGenerator

api_bp = Blueprint("api", __name__, url_prefix="/v1")


@api_bp.route("/health", methods=["GET"])
def health():
    """Health check endpoint."""
    return jsonify(
        {
            "status": "ok",
            "service": "llm-gateway",
            "author": current_app.config["APP_AUTHOR"],
            "providers_count": len(
                current_app.provider_service.get_all_providers()
            ),
        }
    )


@api_bp.route("/models", methods=["GET"])
def list_models():
    """List available models."""
    models = current_app.catalog_service.get_all_models()
    return jsonify({"object": "list", "data": models})


@api_bp.route("/chat/completions", methods=["POST"])
def chat_completions():
    """OpenAI-compatible chat completions endpoint."""
    data = request.get_json(silent=True) or {}
    model = data.get("model", current_app.config.get("DEFAULT_MODEL", "gpt-4o-mini"))
    messages = data.get("messages", [])
    stream = data.get("stream", False)

    # Validate input
    if not messages:
        return jsonify({"error": {"message": "messages is required", "code": "invalid_request_error"}}), 400

    # Resolve provider
    provider = current_app.provider_service.resolve_provider(model)
    if not provider:
        return jsonify(
            {"error": {"message": f"Model '{model}' not found", "code": "model_not_found"}}
        ), 404

    # Check cache if enabled
    if current_app.cache_service and not stream:
        cached = current_app.cache_service.get(
            model, messages,
            temperature=data.get("temperature", 0.7),
        )
        if cached:
            return jsonify(cached)

    # Prepare request payload
    payload = {
        "model": model,
        "messages": messages,
        **{k: v for k, v in data.items() if k not in {"model", "messages"}},
    }

    try:
        if stream:
            return _stream_response(provider, "chat/completions", payload)
        else:
            response = _make_request(provider, "chat/completions", payload)
            if current_app.cache_service:
                current_app.cache_service.set(
                    model, messages, response,
                    temperature=data.get("temperature", 0.7),
                )
            return jsonify(response)
    except Exception as exc:
        return jsonify(
            {"error": {"message": str(exc), "code": "provider_error"}}
        ), 502


@api_bp.route("/completions", methods=["POST"])
def completions():
    """OpenAI-compatible text completions endpoint."""
    data = request.get_json(silent=True) or {}
    model = data.get("model", current_app.config.get("DEFAULT_MODEL", "gpt-4o-mini"))
    prompt = data.get("prompt", "")
    stream = data.get("stream", False)

    if not prompt:
        return jsonify({"error": {"message": "prompt is required", "code": "invalid_request_error"}}), 400

    provider = current_app.provider_service.resolve_provider(model)
    if not provider:
        return jsonify(
            {"error": {"message": f"Model '{model}' not found", "code": "model_not_found"}}
        ), 404

    payload = {"model": model, "prompt": prompt}
    payload.update({k: v for k, v in data.items() if k not in {"model", "prompt"}})

    try:
        if stream:
            return _stream_response(provider, "completions", payload)
        else:
            response = _make_request(provider, "completions", payload)
            return jsonify(response)
    except Exception as exc:
        return jsonify(
            {"error": {"message": str(exc), "code": "provider_error"}}
        ), 502


@api_bp.route("/embeddings", methods=["POST"])
def embeddings():
    """OpenAI-compatible embeddings endpoint."""
    data = request.get_json(silent=True) or {}
    model = data.get("model", current_app.config.get("DEFAULT_MODEL", "gpt-4o-mini"))
    input_value = data.get("input", [])

    if not input_value:
        return jsonify({"error": {"message": "input is required", "code": "invalid_request_error"}}), 400

    provider = current_app.provider_service.resolve_provider(model)
    if not provider:
        return jsonify(
            {"error": {"message": f"Model '{model}' not found", "code": "model_not_found"}}
        ), 404

    payload = {"model": model, "input": input_value}
    payload.update({k: v for k, v in data.items() if k not in {"model", "input"}})

    try:
        response = _make_request(provider, "embeddings", payload)
        return jsonify(response)
    except Exception as exc:
        return jsonify(
            {"error": {"message": str(exc), "code": "provider_error"}}
        ), 502


def _make_request(provider, endpoint: str, payload: dict):
    """Make synchronous request to provider."""
    base = provider.base_url.rstrip("/")
    url = f"{base}/v1/{endpoint}" if not base.endswith("/v1") else f"{base}/{endpoint}"

    headers = {"Content-Type": "application/json"}
    auth_header = provider.get_auth_header()
    if auth_header:
        headers[auth_header[0]] = auth_header[1]

    response = httpx.post(
        url,
        headers=headers,
        json=payload,
        timeout=provider.timeout_ms / 1000,
    )

    if response.status_code >= 400:
        raise RuntimeError(
            f"{provider.name} error {response.status_code}: {response.text}"
        )

    try:
        return response.json()
    except ValueError:
        return {"raw_response": response.text}


def _stream_response(provider, endpoint: str, payload: dict):
    """Stream response from provider."""
    base = provider.base_url.rstrip("/")
    url = f"{base}/v1/{endpoint}" if not base.endswith("/v1") else f"{base}/{endpoint}"

    headers = {"Content-Type": "application/json"}
    auth_header = provider.get_auth_header()
    if auth_header:
        headers[auth_header[0]] = auth_header[1]

    def generate():
        with httpx.stream(
            "POST",
            url,
            headers=headers,
            json=payload,
            timeout=provider.timeout_ms / 1000,
        ) as response:
            if response.status_code >= 400:
                yield f"data: {{"error": \"{response.text}\"}}\n\n".encode()
                return

            for line in response.iter_lines():
                if line:
                    if line.startswith("data: "):
                        yield line.encode() + b"\n"
                    else:
                        yield f"data: {line}".encode() + b"\n"
            yield b"data: [DONE]\n\n"

    return Response(generate(), mimetype="text/event-stream")
