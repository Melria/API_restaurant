from sqlalchemy import create_engine, text
from app.core.config import settings

engine = create_engine(settings.DATABASE_URL)
with engine.connect() as conn:
    result = conn.execute(text("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';"))
    print("Tables in database:")
    for row in result:
        print(row[0])
    
    # Check alembic version
    try:
        version_result = conn.execute(text("SELECT version_num FROM alembic_version;"))
        print("\nAlembic version:")
        for row in version_result:
            print(row[0])
    except:
        print("\nNo alembic_version table found.")