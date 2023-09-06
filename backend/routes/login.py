from fastapi import APIRouter, HTTPException

from crud.users import get_user_by_username
from schemas.user import UserLogin, UserBase
from utils.hash_password import validate_password

router = APIRouter()


@router.post('/login', response_model=UserBase)
async def auth(form_data: UserLogin):
    user = get_user_by_username(username=form_data.username)

    if not user:
        raise HTTPException(status_code=400, detail='Incorrect email or password')

    if not validate_password(
        plain_password=form_data.password, hashed_password=user.password
    ):
        raise HTTPException(status_code=400, detail='Incorrect email or password')

    return user
