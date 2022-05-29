from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from schemas import User
from .routes import users

app = FastAPI(title="BlogAPI")


app.include_router(users.router)
