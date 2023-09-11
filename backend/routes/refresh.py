from typing import Annotated

from fastapi import APIRouter, HTTPException, Cookie
from jose import jwt, JWTError

from config import TokenSettings
from crud import get_user_by_username
from schemas.user import UserAuthResponse, UserResponse
from utils.token import create_access_token

router = APIRouter()


@router.get('/refresh', response_model=UserAuthResponse)
def refresh_token(refresh_token: Annotated[str | None, Cookie()]):
    token_exception = HTTPException(
        status_code=401,
        detail='Could not validate refresh credentials',
        headers={'WWW-Authenticate': 'Bearer'},
    )

    try:
        payload = jwt.decode(refresh_token, TokenSettings.JWT_REFRESH_SECRET_KEY, algorithms=[TokenSettings.ALGORITHM])

        username: str = payload.get("sub")
        if username is None:
            raise token_exception
    except JWTError as e:
        raise token_exception

    user = get_user_by_username(username=username)

    if not user:
        raise token_exception

    return UserAuthResponse(
        user=UserResponse(**user.model_dump(exclude='password')),
        access_token=create_access_token(user.username),
    )
