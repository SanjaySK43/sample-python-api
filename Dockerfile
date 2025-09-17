FROM python:3.11-slim

WORKDIR /app

# Force cache bust with timestamp
ARG CACHEBUST=1

# Install dependencies directly
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir \
        fastapi==0.116.2 \
        uvicorn[standard]==0.35.0 \
        prometheus-client==0.19.0 \
        pytest==7.4.3 \
        httpx==0.25.2 \
        pytest-cov==4.1.0 && \
    pip list && \
    pip show prometheus-client

# Copy application code
COPY main.py .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
