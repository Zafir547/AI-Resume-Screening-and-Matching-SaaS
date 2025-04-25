from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import logging

# Replace with your actual Azure PostgreSQL connection details.
SQLALCHEMY_DATABASE_URL = (
    "postgresql://<username>:<password>@<server-name>.postgres.database.azure.com:5432/<database_name>?sslmode=require"
)
# Logging enable karein
logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

# Engine create
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)  # `echo=True` will log all queries
# engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()    