from fastapi import FastAPI
import models
from models import Base
from models.database import engine
from routers import auth, team, team_member, project, issue


app = FastAPI()

# -> create all DB tables
Base.metadata.create_all(engine)

# -> import All Routers
app.include_router(auth.router)
app.include_router(team.router)
app.include_router(team_member.router)
app.include_router(project.router)
app.include_router(issue.router)
