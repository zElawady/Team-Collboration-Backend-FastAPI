from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from core.config import settings
from typing import Annotated
from fastapi import Depends


engine = create_engine(settings.DB_URL)
Session_local = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()

def get_db():
    db = Session_local()
    try:
        yield db
    finally:
        db.close()

# Depends
db_depends = Annotated[Session, Depends(get_db)]