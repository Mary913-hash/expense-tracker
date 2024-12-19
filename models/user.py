from sqlalchemy import Column, Integer, String
from base import Base  # Import the shared Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f"User(id={self.id}, name={self.name})"
