from typing import Annotated

from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt

from config import TokenSettings
from crud import get_user_by_username
from utils.token import oauth2_scheme


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, TokenSettings.JWT_SECRET_KEY, algorithms=[TokenSettings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = get_user_by_username(username=username)

    if user is None:
        raise credentials_exception

    return user
