# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
import os

# Define the database URL (using SQLite for simplicity, you can switch to other databases like PostgreSQL)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")  # You can change this URL as needed

# Set up the database engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {})

# Create a sessionmaker instance
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative models
Base: DeclarativeMeta = declarative_base()

# Dependency to get the database session
def get_db():
    db = SessionLocal()  # Create a new session
    try:
        yield db  # Yield the session to be used in route handlers
    finally:
        db.close()  # Close the session when done
