from fastapi import FastAPI
from routes import users

app = FastAPI(title='BlogAPI', docs_url='/documentaion')


app.include_router(users.router)
