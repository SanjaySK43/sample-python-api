# Sample Python API

A demonstration Python FastAPI application showcasing modern API development practices with Backstage integration.

## Overview

This sample application demonstrates how to build a Python FastAPI service that integrates seamlessly with Backstage. It serves as a reference implementation for the Python application template and showcases best practices for API development, documentation, and deployment.

## Features

- **FastAPI Framework**: High-performance, easy-to-use web framework
- **Automatic API Documentation**: Interactive docs with Swagger UI and ReDoc
- **Health Monitoring**: Built-in health check endpoints
- **Backstage Integration**: Full catalog integration with metadata and documentation
- **Container Ready**: Docker support for easy deployment
- **Testing Suite**: Comprehensive test coverage with pytest

## Quick Start

### Prerequisites

- Python 3.9+
- pip (Python package manager)
- Docker (optional)

### Installation

1. Clone the repository and navigate to the sample API:
```bash
cd examples/sample-python-api
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install fastapi uvicorn pytest
```

### Running the Application

Start the development server:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The application will be available at:
- API: http://localhost:8000
- Interactive API docs: http://localhost:8000/docs
- Alternative docs: http://localhost:8000/redoc

## API Endpoints

### Core Endpoints

- `GET /` - Welcome message and API information
- `GET /health` - Health check endpoint for monitoring
- `GET /docs` - Interactive API documentation (Swagger UI)
- `GET /redoc` - Alternative API documentation (ReDoc)

### Example Usage

#### Health Check
```bash
curl http://localhost:8000/health
```

Response:
```json
{
  "status": "healthy",
  "timestamp": "2024-01-15T10:30:00Z",
  "version": "1.0.0"
}
```

#### Root Endpoint
```bash
curl http://localhost:8000/
```

Response:
```json
{
  "message": "Welcome to Sample Python API",
  "version": "1.0.0",
  "docs": "/docs"
}
```

## Development

### Project Structure

```
sample-python-api/
├── main.py              # FastAPI application
├── catalog-info.yaml    # Backstage catalog metadata
├── docs/               # Documentation
│   └── index.md        # This documentation
├── mkdocs.yml          # MkDocs configuration
└── tests/              # Test suite
    └── test_main.py    # Application tests
```

### Running Tests

Execute the test suite:
```bash
pytest tests/ -v
```

### Code Quality

The application follows Python best practices:
- **Type Hints**: Full type annotation support
- **Pydantic Models**: Data validation and serialization
- **FastAPI Standards**: RESTful API design patterns
- **Error Handling**: Comprehensive error responses

## Deployment

### Docker Deployment

1. Build the Docker image:
```bash
docker build -t sample-python-api .
```

2. Run the container:
```bash
docker run -p 8000:8000 sample-python-api
```

### Production Considerations

- Configure environment-specific settings
- Set up monitoring and logging
- Enable HTTPS/TLS
- Configure load balancing
- Set up health checks

## Backstage Integration

This sample API is fully integrated with Backstage:

- **Catalog Entry**: Registered as a Component in the software catalog
- **API Definition**: OpenAPI specification available
- **Documentation**: TechDocs integration for this documentation
- **Monitoring**: Health check endpoints for system monitoring
- **Ownership**: Clear ownership and lifecycle management

### Annotations

The following Backstage annotations are configured:

- `backstage.io/techdocs-ref: dir:.` - TechDocs documentation location
- `prometheus.io/scrape: 'true'` - Enable Prometheus monitoring
- `prometheus.io/port: '8000'` - Monitoring port
- `prometheus.io/path: '/metrics'` - Metrics endpoint path

## Extending the API

This sample serves as a foundation for building more complex APIs:

1. **Add Database Integration**: Use SQLAlchemy for data persistence
2. **Implement Authentication**: Add JWT or OAuth2 authentication
3. **Add Business Logic**: Implement domain-specific endpoints
4. **Enhance Monitoring**: Add custom metrics and logging
5. **API Versioning**: Implement versioning strategies

## Support and Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Backstage Documentation](https://backstage.io/docs/)
- [Python Best Practices](https://docs.python.org/3/tutorial/)

## Contributing

This sample API is part of the Backstage Python template ecosystem. Contributions and improvements are welcome through the main repository.

## License

This sample application is provided under the MIT License.
