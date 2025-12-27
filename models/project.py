from models.database import Base
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, func

class Project(Base):
    __tablename__ = 'project'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String)
    team_id = Column(Integer, ForeignKey('team.id'))
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )