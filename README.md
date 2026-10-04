# LLM Gateway - Python Flask

**Author:** Ali Jutt

**Original Project:** [FreeLLMAPI](https://github.com/tashfeenahmed/freellmapi) (TypeScript/Node.js)

A Python Flask-based OpenAI-compatible LLM API gateway that aggregates multiple free and paid LLM providers behind a single `/v1` endpoint.

## Features

- **OpenAI-compatible API** — `/v1/chat/completions`, `/v1/completions`, `/v1/embeddings`
- **Multi-provider support** — Route to 34+ LLM providers
- **Smart routing** — Automatic provider selection based on model and priority
- **Failover support** — Automatic retry with fallback providers
- **Encrypted keys** — AES-256-GCM encryption for API keys
- **Response caching** — Optional in-memory/persistent cache
- **Health checks** — Periodic provider health monitoring
- **Rate limiting** — Per-IP and per-key rate limiting
- **Admin dashboard API** — Manage providers and configuration
- **Streaming** — Support for streaming responses
- **Production-ready** — Docker support, error handling, logging

## Quick Start

### 1. Clone and Setup

```bash
git clone https://github.com/alijutt-xd/llm.git
cd llm
python -m venv venv
```

**Linux/macOS:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

```bash
cp .env.example .env
# Edit .env with your configuration
```

### 4. Run Server

**Development:**
```bash
python app.py
```

**Production:**
```bash
gunicorn -w 4 -b 0.0.0.0:5000 wsgi:app
```

Server will be available at `http://localhost:5000`

## API Endpoints

### Health Check

```bash
curl http://localhost:5000/health
```

Response:
```json
{
  "status": "ok",
  "service": "llm-gateway",
  "author": "Ali Jutt",
  "providers_count": 5
}
```

### List Models

```bash
curl http://localhost:5000/v1/models
```

### Chat Completions

```bash
curl -X POST http://localhost:5000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4o-mini",
    "messages": [
      {"role": "user", "content": "Hello!"}
    ]
  }'
```

### Streaming

```bash
curl -X POST http://localhost:5000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4o-mini",
    "messages": [{"role": "user", "content": "Say hello"}],
    "stream": true
  }'
```

### Admin Endpoints

#### List Providers
```bash
curl http://localhost:5000/admin/providers
```

#### Add Provider
```bash
curl -X POST http://localhost:5000/admin/providers \
  -H "Content-Type: application/json" \
  -d '{
    "name": "my-openai",
    "provider_type": "openai-compatible",
    "base_url": "https://api.openai.com",
    "api_key": "sk-...",
    "models": ["gpt-4o", "gpt-4o-mini"],
    "priority": 1
  }'
```

#### Delete Provider
```bash
curl -X DELETE http://localhost:5000/admin/providers/my-openai
```

## Configuration

All configuration is done via `.env` file. Key variables:

- `PORT` — Server port (default: 5000)
- `HOST` — Server host (default: ::)
- `FLASK_ENV` — Environment (development/production)
- `SECRET_KEY` — Session encryption key
- `ENCRYPTION_KEY` — Provider key encryption key
- `RESPONSE_CACHE` — Enable response caching (true/false)
- `PROXY_RATE_LIMIT_RPM` — Proxy rate limit (requests/minute)
- `PROVIDER_TIMEOUT_DEFAULT` — Default provider timeout (ms)

## Docker

### Build
```bash
docker build -t llm .
```

### Run
```bash
docker run -p 5000:5000 -e SECRET_KEY=your-key llm
```

### Docker Compose
```bash
docker-compose up
```

## Supported Providers

- OpenAI (gpt-4o, gpt-3.5-turbo, etc.)
- Anthropic (Claude, etc.)
- Google (Gemini, etc.)
- Groq (Llama, Mixtral, etc.)
- Mistral
- OpenRouter
- Cohere
- HuggingFace
- Ollama
- Custom OpenAI-compatible endpoints

## Security

- Provider API keys are encrypted with AES-256-GCM
- No secrets logged or exposed in responses
- Rate limiting per IP and per key
- CORS configured for authorized origins only
- Input validation on all endpoints
- Secure error handling without stack trace leakage

## Performance

- Streaming support for efficient large responses
- Connection pooling with persistent HTTP clients
- Response caching with configurable TTL
- Asynchronous background tasks for health checks
- Adaptive timeouts based on provider performance

## Development

### Run Tests
```bash
python -m pytest
```

### Lint Code
```bash
pflake8 llm/
```

### Format Code
```bash
black llm/
```

## Troubleshooting

### Port Already in Use
```bash
lsof -i :5000
kill -9 <PID>
```

### Database Errors
```bash
rm llm.db  # Remove SQLite database and reinitialize
```

### Provider Connection Issues
- Check API key validity
- Verify base URL is correct
- Check network/proxy settings
- Review provider rate limits

## Production Deployment

### Render
1. Push to GitHub
2. Connect repository to Render
3. Set environment variables
4. Deploy

### Railway
1. Push to GitHub
2. Connect repository to Railway
3. Set environment variables
4. Deploy

### VPS/Server
```bash
# Install Python 3.10+
sudo apt install python3 python3-pip

# Clone repository
git clone <repo-url>
cd llm

# Setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Create .env with production settings
cp .env.example .env
# Edit .env

# Run with systemd/supervisor
gunicorn -w 4 -b 0.0.0.0:5000 wsgi:app
```

## License

MIT — See LICENSE file

## Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## Author

**Ali Jutt** — [GitHub](https://github.com/alijutt-xd)

## Original Project

This is a Python/Flask migration of [FreeLLMAPI](https://github.com/tashfeenahmed/freellmapi) by Tashfeen Ahmed.
