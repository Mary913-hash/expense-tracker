from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from base import Base  # Import the shared Base

class Expense(Base):
    __tablename__ = 'expenses'
    
    id = Column(Integer, primary_key=True)
    amount = Column(Integer)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))  # ForeignKey to User table
    category_id = Column(Integer, ForeignKey('categories.id'))  # ForeignKey to Category table
    
    user = relationship("User")
    category = relationship("Category")

    def __repr__(self):
        return f"Expense(id={self.id}, amount={self.amount}, description={self.description}, user_id={self.user_id}, category_id={self.category_id})"
