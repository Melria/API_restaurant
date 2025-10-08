# Stage 1: Build dependencies
FROM python:3.13-slim AS builder

# Env vars (no .pyc, utf-8 everywhere)
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/venv/bin:$PATH"

WORKDIR /app

# Install build deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    libpq-dev \
    libssl-dev \
    libffi-dev \
    python3-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Virtualenv
RUN python -m venv /venv
COPY requirements.txt .
# Install wheel/build tools first so C extensions can be built
RUN /venv/bin/pip install --upgrade pip setuptools wheel cython && \
    /venv/bin/pip install --no-cache-dir -r requirements.txt

# Stage 2: Final image
FROM python:3.13-slim

ENV PATH="/venv/bin:$PATH"

WORKDIR /app

# Copy venv & project
COPY --from=builder /venv /venv
COPY ./app ./app

# Default command = run API
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "app.main:app", "--bind", "0.0.0.0:8000"]
