# Sample Python FastAPI Service

A demonstration Python FastAPI application showcasing Backstage integration with comprehensive monitoring, CI/CD, and documentation.

## 🚀 Features

- **FastAPI Framework**: Modern, fast web framework for building APIs
- **Prometheus Metrics**: Built-in metrics collection and monitoring
- **Grafana Dashboards**: Pre-configured dashboards for visualization
- **Health Checks**: Kubernetes-ready health and readiness endpoints
- **CI/CD Pipeline**: GitHub Actions with testing, linting, and deployment
- **Docker Support**: Multi-stage builds with optimized images
- **Backstage Integration**: Full catalog integration with TechDocs

## 🏃 Quick Start

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Docker Compose (with Monitoring)
```bash
# Start the full stack (API + Prometheus + Grafana)
docker-compose up -d

# Access services:
# - API: http://localhost:8000
# - Prometheus: http://localhost:9090
# - Grafana: http://localhost:3001 (admin/admin)
```

## 📊 Monitoring & Observability

### Prometheus Metrics
- **HTTP Request Rate**: `rate(http_requests_total[5m])`
- **Request Duration**: `http_request_duration_seconds`
- **Application Info**: `app_info`

### Grafana Dashboard
Pre-configured dashboard includes:
- Request rate by endpoint and method
- Response time percentiles (50th, 95th)
- Total request rate gauge
- Error rate monitoring

### API Endpoints

- `GET /` - Welcome message
- `GET /health` - Health check endpoint
- `GET /metrics` - Prometheus metrics (text format)
- `GET /metrics/json` - JSON metrics for basic monitoring
- `GET /docs` - Interactive API documentation (Swagger UI)
- `GET /redoc` - Alternative API documentation (ReDoc)

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
