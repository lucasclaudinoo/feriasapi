from typing import Optional

from pydantic import BaseModel, EmailStr, Field, SecretStr



class UserSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    project: str = Field(...)
    password: SecretStr = Field(...)


    class Config:
        schema_extra = {
            "example": {
                "fullname": "Lucas Botinelly",
                "email": "boti@botinelly.com.br",
                "project": "Beyonder",
                "password": "123abc"
            }
        }


class UpdateUserModel(BaseModel):
    fullname: Optional[str]
    email: Optional[EmailStr]
    project: Optional[str]


    class Config:
        schema_extra = {
           "example": {
                "fullname": "Lucas Botinelly",
                "email": "boti@botinelly.com.br",
                "project": "Thanos",
                "password": "123abc"
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