from pydantic import BaseModel


class DbConfig(BaseModel):
    base: str
    host: str = '127.0.0.1'
    type: str
    user: str
    password: str
    charset: str = 'utf8'
