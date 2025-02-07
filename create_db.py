# create_db.py
from database import engine
from models import Base  # Import only Base

# Create all tables in the database
Base.metadata.create_all(bind=engine)
print("Database tables created successfully!")
