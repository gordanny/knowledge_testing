from datetime import datetime

from sqlalchemy import select

from db.db_conf import database
from models.Token import Token
from models.User import User
from schemas.user import UserBase, UserCreate


def get_user_by_username(username: str):
    query = select(User).where(User.username == username)
    with database.get_session() as session:
        result = session.execute(query).scalars().all()
        return UserCreate.model_validate(result[0]) if result else None


def get_user_by_token(token: str):
    query = select(User).join(Token).where(Token.token == token, Token.expires > datetime.now())
    with database.get_session() as session:
        result = session.execute(query).scalars().all()
        return [UserBase.model_validate(s) for s in result]

