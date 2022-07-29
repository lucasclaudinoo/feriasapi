from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from server.database import retrieve_users
from server.database import (
    add_user,
    delete_user,
    retrieve_user,
    retrieve_users,
    update_user,
)
from server.models.user import (
    ErrorResponseModel,
    ResponseModel,
    UserSchema,
    UpdateUserModel,
)


router = APIRouter()


@router.post("/", response_description="Dados do usuário adicionados ao banco de dados")
async def add_user_data(user: UserSchema = Body(...)):
    user = jsonable_encoder(user)
    new_user = await add_user(user)
    return ResponseModel(new_user, "Usuário adicionado com sucesso")

@router.get("/", response_description="Usuário recuperados")
async def get_users():
    user = await retrieve_users()
    if user:
        return ResponseModel(user, "Usuário recuperados com sucesso")
    return ResponseModel(user, "Lista vazia :(")


@router.get("/{id}", response_description="Dado do usuário retornardo")
async def get_user_data(id):
    user = await retrieve_user(id)
    if user:
        return ResponseModel(user, "Dado do usuário retornardo com sucesso")
    return ErrorResponseModel("Poxa que peninha ocorreu um erro", 404, "o usuário não existe")    


@router.put("/{id}")
async def update_user_data(id: str, req: UpdateUserModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_user = await update_user(id, req)
    if updated_user:
        return ResponseModel(
            "Usuario com o id {} foi atualizado".format(id),
            "Usuario atualizado com sucesso",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the user data.",
    )


@router.delete("/{id}", response_description="Usuario deletado da base de dados")
async def delete_user_data(id: str):
    deleted_user = await delete_user(id)
    if deleted_user:
        return ResponseModel(
            "Usuário com o ID: {} foi romovido".format(id), "Usuário removido com sucesso"
        )
    return ErrorResponseModel(
        "Ocorreu um erro", 404, "Usuário com o id {0} infelizmente não existe".format(id))
    


