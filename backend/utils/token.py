from datetime import datetime, timedelta
from typing import Union, Any

from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import BaseModel

from config import TokenSettings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class TokesSettings(BaseModel):
    lifetime: int
    secret_key: str


def create_access_token(subject: Union[str, Any]) -> str:
    token_settings = TokesSettings(
        lifetime=TokenSettings.ACCESS_TOKEN_EXPIRE_MINUTES,
        secret_key=TokenSettings.JWT_SECRET_KEY
    )
    return create_token(subject, token_settings)


def create_refresh_token(subject: Union[str, Any]) -> str:
    token_settings = TokesSettings(
        lifetime=TokenSettings.REFRESH_TOKEN_EXPIRE_MINUTES,
        secret_key=TokenSettings.JWT_REFRESH_SECRET_KEY
    )
    return create_token(subject, token_settings)


def create_token(subject: Union[str, Any], token_settings: TokesSettings) -> str:
    expires_delta = datetime.utcnow() + timedelta(minutes=token_settings.lifetime)

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, token_settings.secret_key, TokenSettings.ALGORITHM)

    return encoded_jwt
