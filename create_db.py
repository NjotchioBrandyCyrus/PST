from models import User, Savings, Transactions  # Import all models explicitly
from database import engine, Base

Base.metadata.create_all(bind=engine)
print("Database tables created successfully!")
