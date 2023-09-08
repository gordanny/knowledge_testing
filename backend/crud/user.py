from sqlalchemy import select

from db.db_conf import database
from models.User import User
from schemas.user import UserCreate, UserInDBBase
from utils.hash_password import get_hashed_password


def get_user_by_username(username: str):
    query = select(User).where(User.username == username)
    with database.get_session() as session:
        result = session.execute(query).scalars().all()
        return UserInDBBase.model_validate(result[0]) if result else None


def create_user(user: UserCreate):
    with database.get_session() as session:
        instance = User(
            username=user.username,
            fio=user.fio,
            is_admin=user.is_admin,
            password=get_hashed_password(user.password)
        )
        session.add(instance)
        session.commit()

        return UserInDBBase.model_validate(instance)
