from sqlalchemy import create_engine
from models.user import User
from models.category import Category
from models.expense import Expense
from base import Base

# Create an SQLite engine
engine = create_engine('sqlite:///expense_tracker.db')

# Create all tables
Base.metadata.create_all(engine)

print("Database tables created successfully!")
