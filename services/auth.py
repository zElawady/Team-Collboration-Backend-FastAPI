'''
authenticate user ✅

create JWT token ✅

validate token ✅
'''
from models import User
from models.database import db_depends
from core.security import bcrypt, oauth2_bearer, create_jwt, decode_jwt

from core.config import settings
from datetime import timedelta
from typing import Annotated

from fastapi import Security, HTTPException, status





def user_authontication(db:db_depends, user_name:str, password:str):
    user_model = db.query(User).filter(User.user_name == user_name).first()
    if user_model is None:
        return None
    if not bcrypt.verify(password, user_model.hashed_password):
        return None
    return user_model

def login_user(db:db_depends, user_name:str, id:int, role:str):
    token = create_jwt(
        data={'user_name':user_name, 'id':id, 'role':role},
        expire_delta = timedelta(minutes=settings.expire_delta))
    return token

def get_current_user(token:Annotated[str, Security(oauth2_bearer)]):
    try:
        payload = decode_jwt(token)
        user_name:str = payload.get('user_name')
        id:int = payload.get('id')
        role:str = payload.get('role')

        if user_name is None or id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail='invalid token')

        return {'user_name':user_name, 'id':id, 'role':role}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='token validation faild')


user_depends = Annotated[dict, Security(get_current_user)]

