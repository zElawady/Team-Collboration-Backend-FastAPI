'''
Password hashing ✅

JWT encode/decode ✅

Create Tools to help Services ✅
'''

from .config import settings
from jose import jwt
from passlib.context import CryptContext # this is a tool will be used to make hash and varify
from datetime import datetime
from fastapi.security import OAuth2PasswordBearer

bcrypt = CryptContext(schemes=['bcrypt'], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/login")

def hash_password(password:str):
    return bcrypt.hash(password)

def varify_password(password:str, hashed:str):
    return bcrypt.verify(password, hashed)

def create_jwt(data:dict, expire_delta:datetime):
    payload = data.copy()
    expire = datetime.utcnow() + expire_delta
    payload["exp"] = expire
    return jwt.encode(payload,
                      settings.SECRET_KEY,
                      algorithm=settings.ALGORITHM) # this function will return the token

def decode_jwt(token:str):
    return jwt.decode(token,
                      settings.SECRET_KEY,
                      algorithms=settings.ALGORITHM)