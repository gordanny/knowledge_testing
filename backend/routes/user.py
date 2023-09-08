from fastapi import APIRouter, HTTPException

from crud import get_user_by_username
from crud.user import create_user
from schemas.user import UserCreate, UserResponse

router = APIRouter()


@router.post('/create', response_model=UserResponse)
async def create(user: UserCreate):
    db_user = get_user_by_username(username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    created_user = create_user(user=user)
    return UserResponse(**created_user.model_dump(exclude='password'))
