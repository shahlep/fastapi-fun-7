from fastapi import APIRouter, HTTPException, status
from fastapi.encoders import jsonable_encoder
from ..schemas import User, db, UserResponse
from ..utils import get_password_hash
import secrets

router = APIRouter(tags=["Users"])


@router.get("/index")
def index():
    pass


@router.post("/registration",response_model=UserResponse)
async def registration(user_info: User):
    user_info = jsonable_encoder(user_info)

    username_found = await db["users"].find_one({"name": user_info["name"]})
    email_found = await db["users"].find_one({"email": user_info["email"]})

    if username_found:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="username already taken"
        )

    if email_found:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="email already taken"
        )

    user_info["password"] = get_password_hash(user_info["password"])

    # create api key
    user_info["apiKey"] = secrets.token_hex(30)

    new_user = await db["users"].insert_one(user_info)
    created_user = await db["users"].find_one({"_id": new_user.inserted_id})

    return created_user
