<div align="center">

# 🚀 LLM Gateway

**Professional Python Flask project for smart routing, provider management, and OpenAI-compatible LLM access.**

[![Python Version](https://img.shields.io/badge/Python-3.10+-3776ab?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0+-000?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/alijutt-xd/llm?style=flat-square&logo=github)](https://github.com/alijutt-xd/llm)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=flat-square&logo=docker&logoColor=white)](Dockerfile)
[![Termux](https://img.shields.io/badge/Termux-Supported-3DDC84?style=flat-square&logo=android&logoColor=white)](https://termux.com/)
[![Code Style](https://img.shields.io/badge/Code%20Style-PEP%208-1f77b4?style=flat-square)](https://pep8.org/)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen?style=flat-square)](.)

**[Homepage](https://github.com/alijutt-xd/llm)** · **[Features](#features)** · **[Quick Start](#quick-start)** · **[Admin Dashboard](#admin-dashboard)** · **[API Reference](#api-reference)**

</div>

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Quick Start](#quick-start)
  - [Linux/macOS](#linuxmacos)
  - [Windows](#windows)
  - [Termux (Android)](#termux-android)
- [Admin Dashboard](#admin-dashboard)
- [API Reference](#api-reference)
- [Configuration](#configuration)
- [Deployment](#deployment)
- [Security](#security)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

**LLM Gateway** is a production-ready Python Flask application that provides a unified OpenAI-compatible API for routing requests to multiple LLM providers. Manage provider API keys through an intuitive web dashboard, with built-in support for provider testing, health checks, and intelligent request routing.

Inspired by **[FreeLLMAPI](https://github.com/tashfeenahmed/freellmapi)** and optimized for deployment on desktop, server, and mobile platforms including **Termux**.

**Project By:** Ali Jutt

---

## ✨ Features

<table>
<tr>
<td width="50%">

### Core Functionality
- ✅ OpenAI-compatible `/v1` endpoints
- ✅ Multi-provider routing & management
- ✅ Smart provider selection
- ✅ Health check & monitoring
- ✅ Response caching (optional)
- ✅ Streaming support

</td>
<td width="50%">

### Developer Experience
- ✅ REST API & Web Dashboard
- ✅ SQLite persistence
- ✅ Environment-based config
- ✅ Production-ready structure
- ✅ Docker & Gunicorn ready
- ✅ CORS support

</td>
</tr>
<tr>
<td width="50%">

### Security
- ✅ Password-protected admin panel
- ✅ Secure API key storage
- ✅ Rate limiting
- ✅ Input validation
- ✅ HTTPS ready

</td>
<td width="50%">

### Deployment
- ✅ Linux/macOS support
- ✅ Windows support
- ✅ Termux/Android support
- ✅ Docker containers
- ✅ Cloud-ready (Render, Railway)

</td>
</tr>
</table>

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│              LLM Gateway API Server                     │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌─────────────────────────────────────────────────┐  │
│  │  Flask Web Framework                           │  │
│  │  • Routes & Blueprints                         │  │
│  │  • Session Management                          │  │
│  │  • Error Handling                              │  │
│  └─────────────────────────────────────────────────┘  │
│                                                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐ │
│  │   API Tier   │  │ Admin Tier   │  │  Auth Tier  │ │
│  │ /v1/chat     │  │ /admin/*     │  │ /auth/*     │ │
│  │ /v1/complete │  │ Dashboard    │  │ Login       │ │
│  │ /v1/embed    │  │ Provider Mgmt │  │ Logout      │ │
│  └──────────────┘  └──────────────┘  └──────────────┘ │
│                                                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐ │
│  │  Services    │  │  Cache       │  │  Health     │ │
│  │  • Provider  │  │  Service     │  │  Service    │ │
│  │  • Catalog   │  │  • LRU Cache │  │  • Checks   │ │
│  │  • Models    │  │  • TTL       │  │  • Monitor  │ │
│  └──────────────┘  └──────────────┘  └──────────────┘ │
│                                                         │
│  ┌──────────────────────────────────────────────────┐  │
│  │  Database Layer (SQLAlchemy)                   │  │
│  │  • SQLite persistence                          │  │
│  │  • Provider configuration                      │  │
│  │  • API key storage (encrypted)                 │  │
│  └──────────────────────────────────────────────────┘  │
│                                                         │
└─────────────────────────────────────────────────────────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
   ┌─────────┐        ┌─────────┐      ┌─────────┐
   │  OpenAI │        │ Groq    │      │Anthropic│
   │         │        │         │      │         │
   └─────────┘        └─────────┘      └─────────┘
        │                 │                 │
        └─────────────────┼─────────────────┘
              (Provider Routing Layer)
```

**Project Structure:**

```
llm/
├── app.py                     # Flask application factory
├── wsgi.py                    # Gunicorn entry point
├── requirements.txt           # Python dependencies
├── .env.example               # Example environment config
├── Dockerfile                 # Docker configuration
├── docker-compose.yml         # Docker Compose setup
│
├── llm/
│   ├── __init__.py            # App initialization
│   ├── config.py              # Configuration management
│   ├── extensions.py          # Flask extensions
│   ├── models.py              # Data models
│   │
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── api.py             # /v1/* endpoints
│   │   ├── admin.py           # /admin/* endpoints
│   │   └── auth.py            # /auth/* endpoints
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── provider_service.py    # Provider management
│   │   ├── catalog_service.py     # Model catalog
│   │   ├── health_service.py      # Health checks
│   │   └── cache_service.py       # Response caching
│   │
│   ├── lib/
│   │   └── scheduler.py        # Background tasks
│   │
│   ├── templates/admin/
│   │   ├── login.html          # Admin login page
│   │   └── dashboard.html      # Admin dashboard
│   │
│   └── static/                 # Static assets
│
└── .gitignore
```

---

## 🚀 Quick Start

### Requirements

- **Python 3.10+**
- **pip** (Python package manager)
- **Virtual environment** (recommended)
- **Git** (for cloning)

### Linux/macOS

```bash
# Clone repository
git clone https://github.com/alijutt-xd/llm.git
cd llm

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your settings

# Run development server
python app.py
```

**Server running at:** `http://localhost:5000`

### Windows

```bash
# Clone repository
git clone https://github.com/alijutt-xd/llm.git
cd llm

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
copy .env.example .env
# Edit .env with your settings

# Run development server
python app.py
```

**Server running at:** `http://localhost:5000`

### Termux (Android)

Termux brings a full Linux development environment to Android devices.

```bash
# Update package manager
pkg update && pkg upgrade

# Install required packages
pkg install python git clang libffi openssl

# Clone repository
git clone https://github.com/alijutt-xd/llm.git
cd llm

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your settings (nano .env)

# Run server
python app.py
```

**For localhost access from phone:**
```
http://localhost:5000
```

**For network access (other devices on LAN):**

Edit `.env`:
```env
HOST=0.0.0.0
PORT=5000
```

Then access from another device:
```
http://YOUR_ANDROID_IP:5000
```

Find your Android IP:
```bash
ifconfig  # Look for wlan0 inet address
```

---

## 🎛️ Admin Dashboard

The web-based admin dashboard provides full control over providers without command-line interaction.

**Access:** `http://localhost:5000/admin/login`

### Default Credentials

| Field | Value |
|-------|-------|
| **Password** | `admin123` |

⚠️ **Change this immediately in production!**

### Dashboard Features

#### 📊 Statistics
- Total provider count
- Enabled/disabled providers
- Models count
- Rate limit summary

#### 🔑 Provider Management
- **Add Provider:** Configure new LLM provider with API key
- **Edit Provider:** Update existing provider settings
- **Delete Provider:** Remove provider from system
- **Test Provider:** Validate API key and connectivity

#### ⚙️ Provider Configuration

When adding a provider, configure:

- **Provider Name:** Unique identifier (e.g., `openai-main`)
- **Provider Type:** `openai-compatible`, `anthropic`, `google`, etc.
- **Base URL:** Provider API endpoint
- **API Key:** Provider authentication token
- **API Key Header:** Header name (default: `Authorization`)
- **API Key Prefix:** Header prefix (default: `Bearer`)
- **Models:** Supported models (comma-separated)
- **Priority:** Routing priority (lower = higher priority)
- **Timeout:** Request timeout in milliseconds
- **Rate Limit:** Requests per minute
- **Enabled:** Active/inactive toggle

#### 🧪 Provider Testing

Click "Test" to validate:
- API key validity
- Network connectivity
- Provider responsiveness
- HTTP status

---

## 🔌 API Reference

### Base URL
```
http://localhost:5000
```

### Common Headers
```
Content-Type: application/json
```

---

### Health Check

Check server status.

```bash
GET /health
```

**Response:**
```json
{
  "status": "ok",
  "service": "llm-gateway"
}
```

---

### List Models

Get all available models from configured providers.

```bash
GET /v1/models
```

**Response:**
```json
{
  "object": "list",
  "data": [
    {
      "id": "gpt-4o",
      "object": "model",
      "owned_by": "openai",
      "provider": "openai-main",
      "base_url": "https://api.openai.com"
    }
  ]
}
```

---

### Chat Completions

Generate chat responses (OpenAI-compatible).

```bash
POST /v1/chat/completions
Content-Type: application/json

{
  "model": "gpt-4o",
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful assistant."
    },
    {
      "role": "user",
      "content": "What is the capital of France?"
    }
  ],
  "temperature": 0.7,
  "max_tokens": 150
}
```

**Response:**
```json
{
  "id": "chatcmpl-xxx",
  "object": "chat.completion",
  "created": 1696000000,
  "model": "gpt-4o",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "The capital of France is Paris."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 30,
    "completion_tokens": 10,
    "total_tokens": 40
  }
}
```

---

### Chat Completions (Streaming)

Stream chat responses in real-time.

```bash
POST /v1/chat/completions
Content-Type: application/json

{
  "model": "gpt-4o",
  "messages": [
    {"role": "user", "content": "Say hello"}
  ],
  "stream": true
}
```

**Response (Server-Sent Events):**
```
data: {"choices":[{"delta":{"content":"Hello"}}]}

data: {"choices":[{"delta":{"content":" there"}}]}

data: [DONE]
```

---

### Text Completions

Generate text completions.

```bash
POST /v1/completions
Content-Type: application/json

{
  "model": "gpt-4o-mini",
  "prompt": "Write a short poem about Python",
  "max_tokens": 100,
  "temperature": 0.8
}
```

---

### Embeddings

Generate text embeddings.

```bash
POST /v1/embeddings
Content-Type: application/json

{
  "model": "text-embedding-3-small",
  "input": [
    "The capital of France is Paris",
    "Machine learning is awesome"
  ]
}
```

---

### Admin API

Manage providers programmatically.

#### List Providers

```bash
GET /admin/providers
```

#### Add Provider

```bash
POST /admin/providers
Content-Type: application/json

{
  "name": "openai-main",
  "provider_type": "openai-compatible",
  "base_url": "https://api.openai.com",
  "api_key": "sk-...",
  "models": ["gpt-4o", "gpt-4o-mini"],
  "priority": 1,
  "enabled": true
}
```

#### Get Provider

```bash
GET /admin/providers/{name}
```

#### Update Provider

```bash
PUT /admin/providers/{name}
Content-Type: application/json

{
  "api_key": "sk-...",
  "enabled": true,
  "priority": 2
}
```

#### Delete Provider

```bash
DELETE /admin/providers/{name}
```

#### Get Statistics

```bash
GET /admin/stats
```

**Response:**
```json
{
  "providers_count": 5,
  "enabled_providers": 4,
  "models_count": 25,
  "total_rate_limit_rpm": 300,
  "total_rate_limit_tpm": 500000
}
```

#### Test Provider

```bash
POST /admin/api/test
Content-Type: application/json

{
  "provider_name": "openai-main"
}
```

---

## ⚙️ Configuration

Configuration is managed through environment variables in `.env` file.

```bash
cp .env.example .env
nano .env  # or your preferred editor
```

### Essential Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `APP_NAME` | `llm` | Application name |
| `APP_AUTHOR` | `Ali Jutt` | Application author |
| `FLASK_ENV` | `development` | Environment (development/production) |
| `SECRET_KEY` | `dev-secret-key-change-in-production` | Session encryption key |
| `PORT` | `5000` | Server port |
| `HOST` | `::` | Server host (IPv4/IPv6) |

### Security Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `ADMIN_PASSWORD` | `admin123` | Admin dashboard password |
| `ENCRYPTION_KEY` | `change-me-in-production` | API key encryption |
| `DATABASE_URL` | `sqlite:///llm.db` | Database connection |

### Feature Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `RESPONSE_CACHE` | `false` | Enable response caching |
| `RESPONSE_CACHE_TTL_SECONDS` | `3600` | Cache TTL (seconds) |
| `PROXY_RATE_LIMIT_RPM` | `120` | Requests per minute limit |
| `PROVIDER_TIMEOUT_DEFAULT` | `60000` | Timeout (milliseconds) |

### Example `.env`

```env
APP_NAME=llm
APP_AUTHOR=Ali Jutt
FLASK_ENV=production
SECRET_KEY=your_random_secret_key_here
ADMIN_PASSWORD=your_secure_admin_password
PORT=5000
HOST=0.0.0.0
ENCRYPTION_KEY=your_64_char_hex_encryption_key
DATABASE_URL=sqlite:///llm.db
RESPONSE_CACHE=true
RESPONSE_CACHE_TTL_SECONDS=3600
PROXY_RATE_LIMIT_RPM=120
PROVIDER_TIMEOUT_DEFAULT=60000
```

---

## 🚀 Deployment

### Development

```bash
python app.py
```

### Production (Linux/macOS/Windows)

Using Gunicorn (production WSGI server):

```bash
gunicorn --workers 4 --bind 0.0.0.0:5000 wsgi:app
```

With systemd (Linux):

```bash
sudo tee /etc/systemd/system/llm.service > /dev/null << EOF
[Unit]
Description=LLM Gateway
After=network.target

[Service]
Type=notify
User=www-data
WorkingDirectory=/path/to/llm
Environment="PATH=/path/to/llm/venv/bin"
ExecStart=/path/to/llm/venv/bin/gunicorn --workers 4 --bind 0.0.0.0:5000 wsgi:app

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable llm
sudo systemctl start llm
```

### Docker

Build image:
```bash
docker build -t llm:latest .
```

Run container:
```bash
docker run -d \
  --name llm-gateway \
  -p 5000:5000 \
  -e SECRET_KEY=your_secret \
  -e ADMIN_PASSWORD=your_password \
  -v llm-data:/app/data \
  llm:latest
```

Docker Compose:
```bash
docker-compose up -d
```

### Cloud Platforms

#### Render

1. Push to GitHub
2. Create new Web Service on Render
3. Connect repository
4. Set environment variables
5. Deploy

#### Railway

1. Push to GitHub
2. Create new project on Railway
3. Connect GitHub repository
4. Add environment variables
5. Deploy

#### VPS (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv nginx

git clone https://github.com/alijutt-xd/llm.git /opt/llm
cd /opt/llm

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

cp .env.example .env
# Edit .env

# Configure Nginx as reverse proxy
sudo tee /etc/nginx/sites-available/llm > /dev/null << EOF
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
    }
}
EOF

sudo ln -s /etc/nginx/sites-available/llm /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx

# Run with systemd
sudo tee /etc/systemd/system/llm.service > /dev/null << EOF
[Unit]
Description=LLM Gateway
After=network.target

[Service]
User=www-data
WorkingDirectory=/opt/llm
Environment="PATH=/opt/llm/venv/bin"
ExecStart=/opt/llm/venv/bin/gunicorn --workers 4 wsgi:app

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable llm
sudo systemctl start llm
```

---

## 🔒 Security

### Best Practices

✅ **Do:**
- Change `ADMIN_PASSWORD` before production
- Use strong `SECRET_KEY` (generate with `python -c "import secrets; print(secrets.token_hex(32))"`)
- Store `.env` securely (never commit to Git)
- Use HTTPS in production
- Enable rate limiting
- Validate all inputs
- Keep dependencies updated
- Use firewall rules

❌ **Don't:**
- Commit `.env` or API keys to repository
- Use default passwords
- Expose admin panel to untrusted networks
- Log sensitive data
- Use development mode in production
- Disable CORS protection
- Store unencrypted API keys

### API Key Encryption

API keys are stored securely in the database. The encryption key is configured via `ENCRYPTION_KEY` environment variable.

Generate a secure key:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

---

## 🐛 Troubleshooting

### Port Already in Use

```bash
# Linux/macOS
lsof -i :5000
kill -9 <PID>

# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

### Import Errors

```bash
pip install -r requirements.txt
pip install --upgrade pip
```

### Database Errors

```bash
rm llm.db
python app.py
```

### Admin Password Not Working

Check `.env`:
```bash
echo $ADMIN_PASSWORD
```

### Termux Build Issues

```bash
pkg install build-essential openssl libffi clang
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

### Docker Issues

```bash
docker logs llm-gateway
docker exec -it llm-gateway bash
```

---

## 📝 Examples

### Python Client

```python
import requests

BASE_URL = "http://localhost:5000"

# Chat completion
response = requests.post(
    f"{BASE_URL}/v1/chat/completions",
    json={
        "model": "gpt-4o",
        "messages": [
            {"role": "user", "content": "Hello!"}
        ]
    }
)

print(response.json())
```

### JavaScript/Node.js

```javascript
const BASE_URL = "http://localhost:5000";

const response = await fetch(`${BASE_URL}/v1/chat/completions`, {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    model: "gpt-4o",
    messages: [{ role: "user", content: "Hello!" }]
  })
});

console.log(await response.json());
```

### Shell/cURL

```bash
curl -X POST http://localhost:5000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4o",
    "messages": [
      {"role": "user", "content": "Hello from LLM Gateway"}
    ]
  }'
```

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Ali Jutt**

- GitHub: [@alijutt-xd](https://github.com/alijutt-xd)
- Email: alijuttxd@gmail.com

---

## 🙏 Acknowledgments

- Inspired by [FreeLLMAPI](https://github.com/tashfeenahmed/freellmapi) by Tashfeen Ahmed
- Built with [Flask](https://flask.palletsprojects.com/)
- Deployed with [Gunicorn](https://gunicorn.org/)
- Container support via [Docker](https://www.docker.com/)

---

<div align="center">

### ⭐ If you find this project helpful, please consider giving it a star!

Made with ❤️ by **Ali Jutt**

</div>
