# models/category.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from base import Base

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # Relationship to expenses
    expenses = relationship("Expense", back_populates="category")

    def __repr__(self):
        return f"<Category(id={self.id}, name='{self.name}')>"
