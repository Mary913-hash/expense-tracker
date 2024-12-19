# models/expense.py
from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class Expense(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))

    # Relationships
    user = relationship("User", back_populates="expenses")
    category = relationship("Category", back_populates="expenses")

    def __repr__(self):
        return f"<Expense(id={self.id}, amount={self.amount}, description='{self.description}')>"
