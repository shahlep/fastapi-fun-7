from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from ..schemas import User, db

router = APIRouter(tags=["Users"])


@router.get("/index")
def index():
    pass


@router.post("/registration")
async def registration(user_info: User):
    user_info = jsonable_encoder(user_info)
