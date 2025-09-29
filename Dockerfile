# Stage 1: Build dependencies
FROM python:3.12-slim AS builder

# Env vars (no .pyc, utf-8 everywhere)
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/venv/bin:$PATH"

WORKDIR /app

# Install build deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc \
    && rm -rf /var/lib/apt/lists/*

# Virtualenv
RUN python -m venv /venv
COPY requirements.txt .
RUN /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install --no-cache-dir -r requirements.txt

# Stage 2: Final image
FROM python:3.12-slim

ENV PATH="/venv/bin:$PATH"

WORKDIR /app

# Copy venv & project
COPY --from=builder /venv /venv
COPY ./app ./app

# Default command = run API
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "app.main:app", "--bind", "0.0.0.0:8000"]
