from typing import Optional

from pydantic import BaseModel, EmailStr, Field, SecretStr



class AdminSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)


    class Config:
        schema_extra = {
            "example": {
                "fullname": "Osmar",
                "email": "osmarbr@osmar.com.br",
                "password": "1234abc"
            }
        }


class UpdateAdminModel(BaseModel):
    fullname: Optional[str]
    email: Optional[EmailStr]


    class Config:
        schema_extra = {
           "example": {
                "fullname": "Osmar",
                "email": "osmarbr@osmar.com.br",
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}