from pydantic import Field, BaseModel

from schemas.base import BaseFromOrmModel


class UserBase(BaseFromOrmModel):
    username: str


class UserCreate(UserBase):
    fio: str
    is_admin: bool | None = Field(default=False, validation_alias='isAdmin')
    password: str


class UserInDBBase(UserCreate):
    pass


class UserRequest(UserBase):
    pass


class UserLoginRequest(UserRequest):
    password: str


class UserResponse(UserBase):
    fio: str
    is_admin: bool = Field(serialization_alias='isAdmin')


class UserAuthResponse(BaseModel):
    user: UserResponse
    access_token: str = Field(serialization_alias='accessToken')
