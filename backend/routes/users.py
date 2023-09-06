from fastapi import APIRouter, HTTPException

from crud.users import get_user_by_username
from schemas.user import UserBase, UserCreate

router = APIRouter()


@router.post('/sign-up', response_model=UserBase)
async def create_user(user: UserCreate):
    db_user = get_user_by_username(username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return create_user(user=user)
