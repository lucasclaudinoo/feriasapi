import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.users

user_collection = database.get_collection("users_collection")

admin_collection = database.get_collection("admins_collection")



def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "fullname": user["fullname"],
        "email": user["email"],
        "project": user["project"],
        "password": user["password"],
    }

# Recupera todos os usuarios do banco de dados
async def retrieve_users():
    users = []
    async for user in user_collection.find():
        users.append(user_helper(user))
    return users


# adiciona novo usuario ao banco de dados
async def add_user(user_data: dict) -> dict:
    user = await user_collection.insert_one(user_data)
    new_user = await user_collection.find_one({"_id": user.inserted_id})
    return user_helper(new_user)


# Recupera usuario pelo id
async def retrieve_user(id: str) -> dict:
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        return user_helper(user)


# Atualizar usuario pelo id
async def update_user(id: str, data: dict):
    #retorna  falso caso sejo seja enviado vazio 
    if len(data) < 1:
        return False
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        updated_user = await user_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_user:
            return True
        return False


# Deletar usuario do banco de dados
async def delete_user(id: str):
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        await user_collection.delete_one({"_id": ObjectId(id)})
        return True


# Admin
def admin_helper(admin) -> dict:
    return {
        "id": str(admin["_id"]),
        "fullname": admin["fullname"],
        "email": admin["email"],
        "password": admin["password"],
    }


# Recupera todos os admins do banco de dados
async def retrieve_admins():
    admins = []
    async for admin in admin_collection.find():
        admins.append(admin_helper(admin))
    return admins


# adiciona novo admin ao banco de dados
async def add_admin(admin_data: dict) -> dict:
    admin = await admin_collection.insert_one(admin_data)
    new_admin = await admin_collection.find_one({"_id": admin.inserted_id})
    return admin_helper(new_admin)


# Recupera admin pelo id
async def retrieve_admin(id: str) -> dict:
    admin = await admin_collection.find_one({"_id": ObjectId(id)})
    if admin:
        return admin_helper(admin)


# Atualizar admin pelo id
async def update_admin(id: str, data: dict):
    #retorna  falso caso sejo seja enviado vazio 
    if len(data) < 1:
        return False
    admin = await admin_collection.find_one({"_id": ObjectId(id)})
    if admin:
        updated_admin = await admin_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_admin:
            return True
        return False


# Deletar usuario do banco de dados
async def delete_admin(id: str):
    admin = await admin_collection.find_one({"_id": ObjectId(id)})
    if admin:
        await admin_collection.delete_one({"_id": ObjectId(id)})
        return True
