from sqlalchemy import Column, Integer, String
from base import Base  # Import the shared Base

class Category(Base):
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f"Category(id={self.id}, name={self.name})"
