from fastapi import FastAPI

from server.routes.user import router as UserRouter

from server.routes.admin import router as AdminRouter


app = FastAPI()

app.include_router(UserRouter, tags=["User"], prefix="/user")

app.include_router(AdminRouter, tags=["Admin"], prefix="/admin")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": ""}