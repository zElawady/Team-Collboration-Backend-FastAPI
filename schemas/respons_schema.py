from pydantic import BaseModel, Field, field_serializer
from datetime import datetime

class project_respons(BaseModel):
    name:str = Field(max_length=45, min_length=0)
    created_at:datetime

    @field_serializer("created_at")
    def format_created_at(self, value: datetime):
        return value.strftime("%Y-%m-%d %I:%M %p")

class issue_respons(BaseModel):
    title:str = Field(max_length=45, min_length=0)
    description:str = Field(max_length=200, min_length=0)
    status:str = Field(default='closed')
    priority:int = Field(gt=0, lt=6)
    created_at: datetime

    @field_serializer("created_at")
    def format_created_at(self, value: datetime):
        return value.strftime("%Y-%m-%d %I:%M %p")
