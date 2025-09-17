"""
Sample Python FastAPI Application

A demonstration API showcasing FastAPI integration with Backstage.
This serves as a reference implementation for Python services.
"""

from datetime import datetime
from typing import Dict, Any
from fastapi import FastAPI
from pydantic import BaseModel

# Application metadata
__version__ = "1.0.0"

# FastAPI application instance
app = FastAPI(
    title="Sample Python API",
    description="A demonstration Python FastAPI application for Backstage integration",
    version=__version__,
    docs_url="/docs",
    redoc_url="/redoc",
)

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
        message="Welcome to Sample Python API",
        version=__version__,
        docs="/docs"
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
        version=__version__
    )

@app.get("/metrics")
async def metrics() -> Dict[str, Any]:
    """
    Basic metrics endpoint for Prometheus monitoring.
    
    Returns:
        Dict: Basic application metrics
    """
    return {
        "app_info": {
            "name": "sample-python-api",
            "version": __version__
        },
        "health_status": "healthy",
        "uptime_seconds": 0,  # Placeholder - would track actual uptime
        "requests_total": 0,  # Placeholder - would track request count
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
