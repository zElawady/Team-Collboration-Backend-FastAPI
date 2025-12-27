from pydantic import BaseModel, Field, EmailStr, validator

class user_requests(BaseModel):
    user_name:str = Field(max_length=45, min_length=0)
    email:EmailStr
    password:str
    role:str = Field(default='user')
    is_active:bool = Field(default=True)

class team_requests(BaseModel):
    name:str = Field(max_length=45, min_length=0)

class project_requests(BaseModel):
    name:str = Field(max_length=45, min_length=0)

class issue_requests(BaseModel):
    title:str = Field(max_length=45, min_length=0)
    description:str = Field(max_length=200, min_length=0)
    status:str = Field(default='closed')
    priority:int = Field(gt=0, lt=6)
