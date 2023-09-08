from datetime import datetime, timedelta
from typing import Union, Any

from fastapi.security import OAuth2PasswordBearer
from jose import jwt

from config import TokenSettings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    return create_token(subject, TokenSettings.ACCESS_TOKEN_EXPIRE_MINUTES, expires_delta)


def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    return create_token(subject, TokenSettings.REFRESH_TOKEN_EXPIRE_MINUTES, expires_delta)


def create_token(subject: Union[str, Any], token_lifetime: int, expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=token_lifetime)

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, TokenSettings.JWT_REFRESH_SECRET_KEY, TokenSettings.ALGORITHM)

    return encoded_jwt
