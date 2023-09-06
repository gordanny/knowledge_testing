"""Fill users

Revision ID: 23bf9b8ba4f5
Revises: c57a37093a84

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import delete, insert
from sqlalchemy.orm import Session

from models.User import User
from utils.hash_password import hash_password

# revision identifiers, used by Alembic.
revision: str = '23bf9b8ba4f5'
down_revision: Union[str, None] = '04092ba7443f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

users = [
    {
        'username': 'test',
        'password': hash_password('test'),
        'fio': 'Тестер Тестирович Тестеров',
        'is_admin': False
    },
    {
        'username': 'admin',
        'password': hash_password('admin'),
        'fio': 'Админ Админович Админов',
        'is_admin': True
    },
]


def upgrade() -> None:
    session = Session(bind=op.get_bind())
    session.execute(insert(User), users,)
    session.commit()


def downgrade() -> None:
    session = Session(bind=op.get_bind())
    usernames = [user.get('username') for user in users if user]
    statement = delete(User).where(User.username.in_(usernames))
    session.execute(statement)
    session.commit()
