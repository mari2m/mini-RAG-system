from pydantic import BaseModel,Field,validator
from typing import Optional
from bson.objectid import ObjectId

class project(BaseModel):
    _id:Optional(ObjectId)
    project_id:str= Field(...,min_length=1)

    #custum validation
    @validator("project_id")
    def validation_id(cls,value):
        if not value.isalnum():
            raise ValueError("project_id must be alphanumaric")
        return value
    
    class Config:
        arbitrary_type_allowed=True