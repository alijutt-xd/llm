from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for
from functools import wraps
import hashlib
import os
from llm.models import Provider, ProviderType

admin_bp = Blueprint("admin", __name__, url_prefix="/admin", static_folder="static", template_folder="templates")

# Simple password protection decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "admin_logged_in" not in session:
            return redirect(url_for("admin.login_page"))
        return f(*args, **kwargs)
    return decorated_function


@admin_bp.route("/login", methods=["GET", "POST"])
def login_page():
    """Admin login page."""
    if request.method == "POST":
        password = request.form.get("password", "")
        admin_password = os.getenv("ADMIN_PASSWORD", "admin123")
        
        # Hash password for comparison
        if hashlib.sha256(password.encode()).hexdigest() == hashlib.sha256(admin_password.encode()).hexdigest():
            session["admin_logged_in"] = True
            return redirect(url_for("admin.dashboard"))
        else:
            return render_template("admin/login.html", error="Invalid password")
    
    return render_template("admin/login.html")


@admin_bp.route("/logout")
def logout():
    """Logout admin."""
    session.pop("admin_logged_in", None)
    return redirect(url_for("admin.login_page"))


@admin_bp.route("/")
@login_required
def dashboard():
    """Admin dashboard."""
    from flask import current_app
    providers = current_app.provider_service.get_all_providers()
    return render_template(
        "admin/dashboard.html",
        providers=providers,
        provider_types=[pt.value for pt in ProviderType],
    )


@admin_bp.route("/providers", methods=["GET"])
@login_required
def list_providers():
    """List all providers (JSON API)."""
    from flask import current_app
    providers = current_app.provider_service.list_providers()
    return jsonify({"providers": providers})


@admin_bp.route("/providers", methods=["POST"])
@login_required
def add_provider():
    """Add new provider."""
    from flask import current_app
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
            api_key_header=payload.get("api_key_header", "Authorization"),
            api_key_prefix=payload.get("api_key_prefix", "Bearer"),
            enabled=payload.get("enabled", True),
            models=payload.get("models", []),
            priority=payload.get("priority", 100),
            timeout_ms=payload.get("timeout_ms", 60000),
            rate_limit_rpm=payload.get("rate_limit_rpm", 60),
            rate_limit_tpm=payload.get("rate_limit_tpm", 100000),
        )
        current_app.provider_service.add_provider(provider)
        return jsonify({"status": "ok", "provider": provider.to_dict()}), 201
    except Exception as exc:
        return jsonify({"error": str(exc)}), 400


@admin_bp.route("/providers/<name>", methods=["GET"])
@login_required
def get_provider(name):
    """Get provider details."""
    from flask import current_app
    provider = current_app.provider_service.get_provider(name)
    if not provider:
        return jsonify({"error": f"Provider '{name}' not found"}), 404
    return jsonify(provider.to_dict())


@admin_bp.route("/providers/<name>", methods=["PUT"])
@login_required
def update_provider(name):
    """Update provider."""
    from flask import current_app
    payload = request.get_json(silent=True) or {}
    provider = current_app.provider_service.get_provider(name)

    if not provider:
        return jsonify({"error": f"Provider '{name}' not found"}), 404

    # Update fields
    updatable_fields = [
        "enabled", "priority", "timeout_ms", "models",
        "api_key", "rate_limit_rpm", "rate_limit_tpm",
        "api_key_header", "api_key_prefix"
    ]
    for field in updatable_fields:
        if field in payload:
            setattr(provider, field, payload[field])

    return jsonify({"status": "ok", "provider": provider.to_dict()})


@admin_bp.route("/providers/<name>", methods=["DELETE"])
@login_required
def delete_provider(name):
    """Delete provider."""
    from flask import current_app
    if current_app.provider_service.delete_provider(name):
        return jsonify({"status": "deleted", "provider": name})
    else:
        return jsonify({"error": f"Provider '{name}' not found"}), 404


@admin_bp.route("/stats", methods=["GET"])
@login_required
def stats():
    """Get gateway statistics."""
    from flask import current_app
    providers = current_app.provider_service.get_all_providers()
    return jsonify(
        {
            "providers_count": len(providers),
            "enabled_providers": sum(1 for p in providers if p.enabled),
            "models_count": sum(len(p.models) for p in providers),
            "total_rate_limit_rpm": sum(p.rate_limit_rpm for p in providers),
            "total_rate_limit_tpm": sum(p.rate_limit_tpm for p in providers),
        }
    )


@admin_bp.route("/api/test", methods=["POST"])
@login_required
def test_provider():
    """Test provider API key."""
    from flask import current_app
    import httpx
    
    payload = request.get_json(silent=True) or {}
    provider_name = payload.get("provider_name")
    
    provider = current_app.provider_service.get_provider(provider_name)
    if not provider:
        return jsonify({"error": f"Provider '{provider_name}' not found"}), 404
    
    try:
        # Test with a simple models endpoint
        base = provider.base_url.rstrip("/")
        url = f"{base}/v1/models" if not base.endswith("/v1") else f"{base}/models"
        
        headers = {"Content-Type": "application/json"}
        auth_header = provider.get_auth_header()
        if auth_header:
            headers[auth_header[0]] = auth_header[1]
        
        response = httpx.get(
            url,
            headers=headers,
            timeout=10,
        )
        
        if response.status_code == 200:
            return jsonify({"status": "success", "message": "Provider is working"})
        else:
            return jsonify({
                "status": "error",
                "message": f"Provider returned {response.status_code}",
                "details": response.text[:200]
            }), 400
    except Exception as exc:
        return jsonify({
            "status": "error",
            "message": str(exc)
        }), 400
