from models.database import Base
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, func

class Issue(Base):
    __tablename__ = 'issue'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    title = Column(String)
    description = Column(String, nullable=True)
    status = Column(String, default='closed')
    priority = Column(Integer)
    project_id = Column(Integer, ForeignKey('project.id'))
    assigned_to = Column(Integer, ForeignKey('users.id'), nullable=True)
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )