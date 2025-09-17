"""
Sample Python FastAPI Application

A demonstration API showcasing FastAPI integration with Backstage.
This serves as a reference implementation for Python services.
"""

import time
from datetime import datetime
from typing import Any, Dict

from fastapi import FastAPI, Request
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response
from pydantic import BaseModel

# Application metadata
__version__ = "1.0.0"

# Prometheus metrics
REQUEST_COUNT = Counter(
    "http_requests_total", "Total HTTP requests", ["method", "endpoint", "status_code"]
)
REQUEST_DURATION = Histogram(
    "http_request_duration_seconds",
    "HTTP request duration in seconds",
    ["method", "endpoint"],
)
APP_INFO = Counter("app_info", "Application information", ["version", "name"])

# FastAPI application instance
app = FastAPI(
    title="Sample Python API",
    description="A demonstration Python FastAPI application for Backstage integration",
    version=__version__,
    docs_url="/docs",
    redoc_url="/redoc",
)

# Initialize app info metric
APP_INFO.labels(version=__version__, name="sample-python-api").inc(0)


# Middleware for metrics collection
@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    # Record metrics
    duration = time.time() - start_time
    REQUEST_DURATION.labels(method=request.method, endpoint=request.url.path).observe(
        duration
    )
    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=request.url.path,
        status_code=response.status_code,
    ).inc()

    return response


# Response models
class HealthResponse(BaseModel):
    status: str
    timestamp: str
    version: str


class WelcomeResponse(BaseModel):
    message: str
    version: str
    docs: str


@app.get("/", response_model=WelcomeResponse)
async def root() -> WelcomeResponse:
    """
    Root endpoint providing API information and welcome message.

    Returns:
        WelcomeResponse: Welcome message with API details
    """
    return WelcomeResponse(
        message="Welcome to Sample Python API", version=__version__, docs="/docs"
    )


@app.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    """
    Health check endpoint for monitoring and load balancer probes.

    Returns:
        HealthResponse: Current health status and metadata
    """
    return HealthResponse(
        status="healthy",
        timestamp=datetime.utcnow().isoformat() + "Z",
        version=__version__,
    )


@app.get("/metrics")
async def get_metrics():
    """
    Prometheus metrics endpoint.

    Returns:
        Response: Prometheus formatted metrics
    """
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)


@app.get("/metrics/json")
async def get_metrics_json() -> Dict[str, Any]:
    """
    JSON metrics endpoint for basic monitoring.

    Returns:
        Dict: Basic application metrics in JSON format
    """
    return {
        "app_info": {"name": "sample-python-api", "version": __version__},
        "health_status": "healthy",
        "uptime_seconds": 0,  # Placeholder - would track actual uptime
        "requests_total": 0,  # Placeholder - would track request count
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
