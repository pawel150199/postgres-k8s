from sqlalchemy import Column, Integer, stringformat
from sqlalchemy.orm import relationship
from app.db import Base

class UserModel(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    f_name = Column(String)
    l_name = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    todos = relationship("TodoModel", back_populates="owner", cascade="all, delete-orphan")