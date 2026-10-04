# llm

Author: ALi Jutt

A Python Flask project that exposes an OpenAI-compatible API for routing requests to multiple free or custom LLM providers behind a single `/v1` endpoint.

## Features
- OpenAI-compatible `/v1/chat/completions`
- OpenAI-compatible `/v1/models`
- OpenAI-compatible `/v1/completions`
- OpenAI-compatible `/v1/embeddings`
- Multi-provider registry
- Smart routing by model
- Automatic failover support
- Encrypted provider API keys
- Health endpoint
- Admin provider registration

## Quick start

1. Create a virtual environment
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Create your environment file
   ```bash
   cp .env.example .env
   ```

4. Update your provider config
   Edit `llm/data/providers.json` and set a real API base URL and key.

5. Run the app
   ```bash
   python app.py
   ```

## API examples

### Health check
```bash
curl http://localhost:5000/v1/health
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
      {"role": "user", "content": "Hello from llm"}
    ]
  }'
```

### Add a provider
```bash
curl -X POST http://localhost:5000/admin/providers \
  -H "Content-Type: application/json" \
  -d '{
    "name": "my-provider",
    "base_url": "https://example.com/v1",
    "api_key": "my-key",
    "enabled": true,
    "models": ["gpt-4o-mini", "llama-3.1-70b"],
    "priority": 2
  }'
```

## Notes
- The project is intentionally designed to act like a central OpenAI-compatible gateway.
- The default provider is disabled to prevent accidental requests.
- API keys are encrypted before being written to the provider config.

## License
This project is provided for personal experimentation and local use.
