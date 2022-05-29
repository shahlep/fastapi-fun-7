from fastapi import FastAPI

from .routes import users

app = FastAPI(title="BlogAPI")


app.include_router(users.router)
