from models.database import Base
from sqlalchemy import Column, String, Integer, Boolean

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    user_name = Column(String, unique=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    role = Column(String, default='user')
    is_active = Column(Boolean, default=True)
