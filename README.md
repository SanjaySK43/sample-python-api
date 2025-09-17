# Sample Python FastAPI Service

A demonstration Python FastAPI application integrated with Backstage.

## Features

- FastAPI framework
- Health check endpoints
- Metrics for monitoring
- Comprehensive test suite
- CI/CD with GitHub Actions
- Docker support

## Quick Start

```bash
# Install dependencies
pip install fastapi uvicorn

# Run the application
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## API Endpoints

- `GET /` - Welcome message
- `GET /health` - Health check
- `GET /metrics` - Application metrics
- `GET /docs` - Interactive API documentation

## Testing

```bash
pip install pytest httpx
pytest tests/
```

## Backstage Integration

This service is registered in Backstage with:
- Component metadata
- TechDocs documentation
- CI/CD workflow monitoring
- Health checks
