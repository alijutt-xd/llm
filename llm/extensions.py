def register_extensions(app):
    app.config.setdefault("JSON_SORT_KEYS", False)
    return app
