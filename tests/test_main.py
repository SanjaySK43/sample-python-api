"""
Test suite for the Sample Python API
"""

import os
import sys

# Add the parent directory to the path to import main
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_root_endpoint():
    """Test the root endpoint returns welcome message"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Welcome to Sample Python API"
    assert data["version"] == "1.0.0"
    assert data["docs"] == "/docs"


def test_health_check():
    """Test the health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["version"] == "1.0.0"
    assert "timestamp" in data


def test_prometheus_metrics_endpoint():
    """Test the Prometheus metrics endpoint"""
    response = client.get("/metrics")
    assert response.status_code == 200
    assert "text/plain" in response.headers["content-type"]
    # Check for Prometheus format
    content = response.content.decode()
    assert "http_requests_total" in content
    assert "http_request_duration_seconds" in content


def test_json_metrics_endpoint():
    """Test the JSON metrics endpoint"""
    response = client.get("/metrics/json")
    assert response.status_code == 200
    data = response.json()
    assert "app_info" in data
    assert data["app_info"]["name"] == "sample-python-api"
    assert data["app_info"]["version"] == "1.0.0"
    assert data["health_status"] == "healthy"


def test_docs_endpoint():
    """Test that API docs are accessible"""
    response = client.get("/docs")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]


def test_redoc_endpoint():
    """Test that ReDoc is accessible"""
    response = client.get("/redoc")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
