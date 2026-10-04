#!/usr/bin/env python3
"""Production entry point using gunicorn."""
from llm import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
