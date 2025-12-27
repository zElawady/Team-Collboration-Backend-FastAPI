from models.database import Base
from sqlalchemy import Column, String, Integer, ForeignKey

class Team(Base):
    __tablename__ = 'team'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, unique=True)
    owner_id = Column(Integer, ForeignKey('users.id'))