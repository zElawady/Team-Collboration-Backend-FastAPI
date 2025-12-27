from fastapi.routing import APIRouter
from models import db_depends
from services.auth import user_depends
from fastapi import status, HTTPException
from crud import new_team
from schemas import team_requests
from crud import get_all_teams


router = APIRouter(prefix='/team', tags=['Team'])


# End_points
## -> POST
@router.post('/new', status_code=status.HTTP_201_CREATED)
async def create_new_team(db:db_depends,
                          user:user_depends,
                          team:team_requests):
    if user is None or user.get('role') != 'admin':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid user")
    new_team(db, team, user.get('id'))
    return 'Done✅'

## -> GET
@router.get('/all_teams', status_code=status.HTTP_200_OK)
async def all_teams(db:db_depends,
                    user:user_depends):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Invalid user')
    return get_all_teams(db, user.get('id'))