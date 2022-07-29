from http.client import HTTPException
from fastapi import APIRouter, Body, Form, status
from fastapi.encoders import jsonable_encoder
from rsa import verify
from server.security import create_token_jwt, verify_password
from server.database import retrieve_admin
from server.database import (
    admin_collection,
    add_admin,
    delete_admin,
    retrieve_admins,
    retrieve_admin,
)
from server.models.admin import (
    AdminSchema,
    ErrorResponseModel,
    ResponseModel,
    AdminSchema,
)


router = APIRouter()


@router.post("/", response_description="Dados do Administrador adicionados ao banco de dados")
async def add_admin_data(admin: AdminSchema = Body(...)):
    admin = jsonable_encoder(admin)
    new_admin = await add_admin(admin)
    return ResponseModel(new_admin, "Administrador adicionado com sucesso")

@router.get("/", response_description="Administradores recuperados")
async def get_admins():
    admin = await retrieve_admins()
    if admin:
        return ResponseModel(admin, "Administradores recuperados com sucesso")
    return ResponseModel(admin, "Lista vazia :(")


@router.get("/{id}", response_description="Dado do admin retornardo")
async def get_admin_data(id):
    admin = await retrieve_admin(id)
    if admin:
        return ResponseModel(admin, "Dado do admin retornardo com sucesso")
    return ErrorResponseModel("Poxa que peninha ocorreu um erro", 404, "o admin não existe")    


@router.delete("/{id}", response_description="admin deletado da base de dados")
async def delete_admin_data(id: str):
    deleted_admin = await delete_admin(id)
    if deleted_admin:
        return ResponseModel(
            "Admin com o ID: {} foi romovido".format(id), "Admin removido com sucesso"
        )
    return ErrorResponseModel(
        "Ocorreu um erro", 404, "Admin com o id {0} infelizmente não existe".format(id))
    
#@router.post("/login")
#async def login(username: str = Form(...), password: str = Form(...)):
 #       admin = admin_collection.find_one(email=username)
 #       if admin:
 #               password = not admin or not verify_password(password, admin['password'])
 #               if not password:
 #                   raise HTTPException(
#                        status_code=status.HTTP_401_UNAUTHORIZED,
#                        detail="Incorrect email or password"
#                    )
#        return {
#            "acess_token": create_token_jwt(admin.id),
#            "token_type": "bearer",
#        }