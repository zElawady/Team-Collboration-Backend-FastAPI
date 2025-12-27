from fastapi.routing import APIRouter
from models import db_depends
from services.auth import user_depends

from fastapi import status, HTTPException
from schemas import team_requests
from crud import add_member

router = APIRouter(prefix='/team_member', tags=['Team_member'])

# End_points
## -> POST
@router.post('/add_member/{user_id}/{team_id}',status_code=status.HTTP_201_CREATED)
async def new_member(db:db_depends,
                     user:user_depends,
                     user_id:int,
                     team_id:int):
    if user is None or user.get('role') != 'admin':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid user")

    add_member(db,user_id,team_id)
    return {'message':'Done✅'}

