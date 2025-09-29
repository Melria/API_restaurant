from celery import Celery
import os

# Chargement des variables d'env
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

celery_app = Celery(
    "restaurant_worker",
    broker=REDIS_URL,
    backend=REDIS_URL
)

# Détection auto des tâches dans app/tasks/
celery_app.autodiscover_tasks(["app.tasks"])
