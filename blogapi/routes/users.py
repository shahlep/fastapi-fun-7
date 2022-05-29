from fastapi import APIRouter

router = APIRouter(tags=["Users"])


@router.get("/index")
def index():
    pass
