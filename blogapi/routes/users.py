from fastapi import APIRouter,HTTPException,status
from fastapi.encoders import jsonable_encoder
from ..schemas import User, db

router = APIRouter(tags=["Users"])


@router.get("/index")
def index():
    pass


@router.post("/registration")
async def registration(user_info: User):
    user_info = jsonable_encoder(user_info)

    username_found = await db['users'].find_one({'name':user_info['name']})
    email_found = await db['users'].find_one({'email':user_info['email']})

    if username_found:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail='username already taken')

    if email_found:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail='email already taken')
