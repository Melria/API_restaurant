from app.worker import celery_app
import time


@celery_app.task
def process_order(order_id: int):
    # Simulation d'un traitement long
    time.sleep(5)
    return {"status": "completed", "order_id": order_id}
