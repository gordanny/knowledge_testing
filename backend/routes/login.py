from fastapi import APIRouter, HTTPException
from starlette.responses import JSONResponse

from crud.user import get_user_by_username
from schemas.user import UserLoginRequest, UserAuthResponse, UserResponse
from utils.hash_password import verify_password
from utils.token import create_access_token, create_refresh_token

router = APIRouter()


@router.post('/login', response_model=UserAuthResponse)
async def login(form_data: UserLoginRequest):
    user = get_user_by_username(username=form_data.username)

    if not user:
        raise HTTPException(status_code=400, detail='Incorrect username or password')

    if not verify_password(
        plain_password=form_data.password, hashed_password=user.password
    ):
        raise HTTPException(status_code=400, detail='Incorrect username or password')

    content = UserAuthResponse(
        user=UserResponse(**user.model_dump(exclude='password')),
        access_token=create_access_token(user.username),
    )
    response = JSONResponse(content=content.model_dump(by_alias=True))
    response.set_cookie(key="refresh_token", value=create_refresh_token(user.username))

    return response
