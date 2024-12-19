from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from base import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # Relationship to expenses
    expenses = relationship("Expense", back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}')>"
