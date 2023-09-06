from pydantic import Field, BaseModel

from schemas.base import BaseFromOrmModel
from schemas.token import TokenBase


class UserLogin(BaseModel):
    username: str
    password: str


class UserBase(BaseFromOrmModel):
    username: str
    fio: str
    is_admin: bool | None = Field(default=False)


class UserCreate(UserBase):
    password: str


class UserWithToken(UserBase):
    token: TokenBase | None = {}
