import os

from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.tasks.orders import process_order


app = FastAPI()


DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql+psycopg2://postgres:postgres@db:5432/restaurant_db"
)


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


@app.get("/")
def root():
    return {"msg": "Restaurant API is running 🚀"}


@app.post("/orders/{order_id}/process")
def run_order(order_id: int):
    task = process_order.delay(order_id)
    return {"task_id": task.id, "status": "processing"}
