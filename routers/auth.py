from fastapi.routing import APIRouter
from crud import create_new_user
from schemas import user_requests

from fastapi import status, Depends, HTTPException
from models import db_depends, ResponseEnume
from typing import Annotated

from fastapi.security import OAuth2PasswordRequestForm
from services.auth import login_user, user_authontication

router = APIRouter(prefix='/auth', tags=['Auth'])

# End_Points
## -> POST
@router.post('/register', status_code=status.HTTP_201_CREATED)
async def create_user(db:db_depends,
                      user:user_requests):
    return create_new_user(db, user)

@router.post('/login', status_code=status.HTTP_200_OK)
async def user_login(db:db_depends,
                forme:Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = user_authontication(db, forme.username, forme.password)
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=ResponseEnume.INVALID_USER.value)
    token = login_user(db, user.user_name, user.id, user.role  )
    return {
        "message": "Welcome! 🎉 Login successful",
        "access_token": token,
        "token_type": "bearer"
    }
