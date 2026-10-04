# LLM Gateway

Professional Python Flask project for smart routing, provider management, and OpenAI-compatible LLM access.

Project Name: llm
Author: Ali Jutt

This repository is a Python Flask implementation inspired by the architecture of FreeLLMAPI, designed for multi-provider LLM routing behind a single OpenAI-compatible API.

## Overview

LLM Gateway provides:

- OpenAI-compatible endpoints for chat, completion, and embeddings
- Multi-provider routing and provider management
- Admin dashboard for adding and testing provider API keys
- Password-protected admin access
- Environment-based configuration
- Support for local development and Termux-based Android deployment
- Docker and gunicorn production deployment support

## Features

- Flask server with production-ready structure
- /v1/chat/completions support
- /v1/completions support
- /v1/embeddings support
- /health status endpoint
- provider registry and routing management
- secure admin interface for provider key management
- optional response caching
- environment configuration using .env
- CORS support
- Docker-ready deployment
- mobile-friendly and lightweight installation

## Project Structure

```text
llm/
├── app.py
├── wsgi.py
├── requirements.txt
├── .env.example
├── Dockerfile
├── docker-compose.yml
├── README.md
├── llm/
│   ├── __init__.py
│   ├── config.py
│   ├── extensions.py
│   ├── models.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── api.py
│   │   ├── admin.py
│   │   └── auth.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── cache_service.py
│   │   ├── catalog_service.py
│   │   ├── health_service.py
│   │   └── provider_service.py
│   ├── lib/
│   │   └── scheduler.py
│   ├── templates/
│   │   └── admin/
│   │       ├── login.html
│   │       └── dashboard.html
│   └── static/
└── .gitignore
```

## Requirements

- Python 3.10+
- pip
- virtualenv (recommended)
- Optional: Android/Termux environment
- Optional: Docker

## Installation

### Standard Linux / macOS

```bash
git clone https://github.com/alijutt-xd/llm.git
cd llm
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

### Windows

```bash
git clone https://github.com/alijutt-xd/llm.git
cd llm
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

### Termux (Android)

Termux is supported for running the project on Android devices.

```bash
pkg update
pkg install python git clang libffi openssl
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
cp .env.example .env
```

For local access from a phone browser:

```bash
python app.py
```

Then open:

- http://localhost:5000
- http://127.0.0.1:5000

If you want external access from another device on the same network, run:

```bash
export HOST=0.0.0.0
python app.py
```

Then access using your device IP:

```bash
http://YOUR_ANDROID_IP:5000
```

## Environment Configuration

Create `.env` from `.env.example` and update the values.

```bash
cp .env.example .env
```

Example variables:

```env
APP_NAME=llm
APP_AUTHOR=Ali Jutt
SECRET_KEY=your_secret_key_here
PORT=5000
HOST=0.0.0.0
FLASK_ENV=development
DATABASE_URL=sqlite:///llm.db
ENCRYPTION_KEY=your_encryption_key_here
ADMIN_PASSWORD=admin123
```

Security note:

- Always change the default admin password before deployment.
- Never commit real API keys to GitHub.
- Use a strong secret key in production.

## Running the Project

### Development

```bash
python app.py
```

### Production with Gunicorn

```bash
gunicorn --bind 0.0.0.0:5000 wsgi:app
```

### Docker

```bash
docker build -t llm .
docker run -p 5000:5000 llm
```

or

```bash
docker-compose up --build
```

## Admin Panel

The project includes a password-protected admin dashboard that allows you to:

- add providers
- edit provider settings
- remove providers
- test provider keys
- view provider stats

Access:

```text
http://localhost:5000/admin/login
```

Default admin password:

```text
admin123
```

Change this in `.env`:

```env
ADMIN_PASSWORD=your_secure_password
```

## API Usage

### Health check

```bash
curl http://localhost:5000/health
```

Example response:

```json
{
  "status": "ok",
  "service": "llm-gateway"
}
```

### List models

```bash
curl http://localhost:5000/v1/models
```

### Chat completions

```bash
curl -X POST http://localhost:5000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4o-mini",
    "messages": [
      {"role": "user", "content": "Hello from LLM Gateway"}
    ]
  }'
```

### Completions

```bash
curl -X POST http://localhost:5000/v1/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4o-mini",
    "prompt": "Write a short greeting",
    "max_tokens": 100
  }'
```

### Embeddings

```bash
curl -X POST http://localhost:5000/v1/embeddings \
  -H "Content-Type: application/json" \
  -d '{
    "model": "text-embedding-3-small",
    "input": ["hello world", "goodbye world"]
  }'
```

## Provider Management

Providers can be managed from the admin panel or via API requests.

### Add a provider

```bash
curl -X POST http://localhost:5000/admin/providers \
  -H "Content-Type: application/json" \
  -d '{
    "name": "openai-test",
    "provider_type": "openai-compatible",
    "base_url": "https://api.openai.com",
    "api_key": "sk-xxxxxxxx",
    "api_key_header": "Authorization",
    "api_key_prefix": "Bearer",
    "models": ["gpt-4o", "gpt-4o-mini"],
    "priority": 1,
    "enabled": true,
    "timeout_ms": 60000,
    "rate_limit_rpm": 60
  }'
```

### Delete a provider

```bash
curl -X DELETE http://localhost:5000/admin/providers/openai-test
```

### List providers

```bash
curl http://localhost:5000/admin/providers
```

## Security Notes

- Admin dashboard is protected by a password
- Provider API keys should be stored securely
- Production should use a strong SECRET_KEY and ADMIN_PASSWORD
- Avoid exposing sensitive data in logs
- Use HTTPS in production

## Production Deployment Advice

For production deployment:

- change SECRET_KEY
- change ADMIN_PASSWORD
- set HOST to 0.0.0.0
- use a reverse proxy like Nginx or Caddy
- enable HTTPS
- use gunicorn workers
- backup .env and database files

## Troubleshooting

### Port already in use

```bash
lsof -i :5000
```

Then kill the process or change the port in `.env`.

### Termux issues

If pip install fails:

```bash
pkg upgrade
pkg install build-essential openssl libffi clang
```

### Module import errors

```bash
pip install -r requirements.txt
```

### Admin login not working

Check the value in `.env`:

```env
ADMIN_PASSWORD=your_secure_password
```

## License

MIT License

## Author

Ali Jutt

## Original Inspiration

This project is inspired by and modeled after the functionality of FreeLLMAPI while being implemented in Python Flask.
