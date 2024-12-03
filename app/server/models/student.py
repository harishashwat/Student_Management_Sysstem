from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class StudentSchema(BaseModel):
    name: str = Field(...)
    age: int = Field(...)
    city: str = Field(...)
    country: str = Field(...)
     
    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "age": 24,
                "city": "Chicago",
                "country":"USA"
            }
        }   
    

class UpdateStudentModel(BaseModel):
    name: Optional[str]
    age: Optional[int]
    city: Optional[str]
    country: Optional[str]
    
     
    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "age": 24,
                "city": "Chicago",
                "country":"USA"
            }
        }  


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 201,
        "message": message,
    }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}