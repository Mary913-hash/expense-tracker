from sqlalchemy import Column, Integer, String
from base import Base  # Import the shared Base

class Login(Base):
    __tablename__ = 'logins'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    def __repr__(self):
        return f"<Login(id={self.id}, username='{self.username}')>"
