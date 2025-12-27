from fastapi.routing import APIRouter
from models.database import db_depends

from services.auth import user_depends
from fastapi import status, HTTPException

from crud import add_project, get_all_projects
from schemas import project_requests, project_respons

from typing import List

router = APIRouter(prefix='/project', tags=['Project'])

# End_points
## -> POST
@router.post('/add_project/{team_id}',
             status_code=status.HTTP_201_CREATED,
             response_model=project_respons)
async def add_new_project(db:db_depends,
                      user:user_depends,
                      project:project_requests,
                      team_id:int):
    if user is None or user.get('role') != 'admin':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid user")

    new_project = add_project(db,project, team_id)
    return new_project



## -> GET
@router.get('/all_projects/{team_id}',
            status_code=status.HTTP_200_OK,
            response_model=List[project_respons])
async def read_all_projects(db:db_depends,
                            user:user_depends,
                            team_id:int):
    if user is None or user.get('role') != 'admin':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid user")

    projects = get_all_projects(db, team_id)
    return projects
