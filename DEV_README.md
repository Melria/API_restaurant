# DEV_README.md - API Restaurant Development Guide

This file summarizes key commands for setting up, running, and maintaining the API Restaurant project (FastAPI-based). Follow these steps for local development and CI/CD. The project now uses Python 3.12.

## Prerequisites
- Python 3.12+
- Docker and Docker Compose
- Git
- VS Code (recommended) with extensions for Black, isort, and flake8

## Project Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd API_restaurant

   python -m venv .venv

Create a virtual environment: 
# On Windows:
.\.venv\Scripts\Activate.ps1
# On macOS/Linux:
source .venv/bin/activate

Install dependencies:
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
pip install -r dev-requirements.txt  # For development tools

With Docker Compose (recommended for full stack):
docker-compose up -d
# Access at http://localhost:8000
# Stop: docker-compose down

With Docker only:
docker build -t api_restaurant:latest .
docker run -d -p 8000:8000 api_restaurant:latest
# Access at http://localhost:8000

Without Docker (for development):
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
# Access at http://localhost:8000

Development Commands
  Run tests:  
    pytest
# Or with coverage: pytest --cov=app

Lint and format code:
flake8 .                    # Lint for style/errors
black .                     # Auto-format code
isort .                     # Sort imports
# Check only (for CI):
black --check .
isort --check-only .

Generate license report:
pip-licenses --format=json > licenses.json

Run security scans:
bandit -r .                 # Scan for vulnerabilities
safety check                # Check dependencies for CVEs
detect-secrets scan         # Scan for secrets

Interactive shell in container:
docker-compose exec web /bin/sh

CI/CD Workflow
Trigger: Automatically on push/PR to main branch via GitHub Actions (.github/workflows/DevSecOps.yml).
Jobs:
build: Builds Docker image, runs tests/linters, scans with Dockle.
dev_checks: Installs dev tools, runs advanced linting, security scans, and license checks.
Manual checks:
    # Before committing:
black --check . && isort --check-only . && flake8 . && pytest    

Committing Changes
    git add .
git commit -m "feat: add new feature"
git push

Recommended Pre-Push Routine
Run this locally in your terminal (with the virtual environment activated):

    # Format and check code
black --check . && isort --check-only . && flake8 .

# Run tests
pytest

# Optional: Security scans
bandit -r . && safety check && detect-secrets scan
