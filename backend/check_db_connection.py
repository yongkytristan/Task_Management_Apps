from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError

# URI from config.py
DATABASE_URI = 'postgresql://postgres:postgres123@localhost/task_db'

try:
    print(f"Attempting to connect to: {DATABASE_URI}")
    engine = create_engine(DATABASE_URI)
    connection = engine.connect()
    print("✅ Connection successful!")
    connection.close()
except OperationalError as e:
    print(f"❌ Connection failed: {e}")
    print("\nPlease ensure:")
    print("1. PostgreSQL is running.")
    print("2. The database 'task_db' exists.")
    print("3. Credentials (postgres/postgres123) are correct.")
except Exception as e:
    print(f"❌ An error occurred: {e}")
