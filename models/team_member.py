from models.database import Base
from sqlalchemy import Column, Integer, ForeignKey

class Team_member(Base):
    __tablename__ = 'team_member'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    team_id = Column(Integer, ForeignKey('team.id'))