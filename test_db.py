from sqlalchemy import create_engine, text
from app.core.config import settings

print(f"DATABASE_URL: {settings.DATABASE_URL}")
try:
    engine = create_engine(settings.DATABASE_URL)
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        print("Connection successful! Database is accessible.")
        print(f"Test query result: {result.fetchone()}")
except Exception as e:
    print(f"Connection failed: {e}")