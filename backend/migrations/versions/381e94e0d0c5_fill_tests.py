"""Fill tests

Revision ID: 381e94e0d0c5
Revises: 11302e94d015

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import delete, insert
from sqlalchemy.orm import Session

from models.Test import Test

# revision identifiers, used by Alembic.
revision: str = '381e94e0d0c5'
down_revision: Union[str, None] = '11302e94d015'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

tests = [
    'Первый тест',
    'Тест №2',
    'Третий тест',
    'Тест №4',
]


def upgrade() -> None:
    session = Session(bind=op.get_bind())
    session.execute(insert(Test), [{'description': test} for test in tests],)
    session.commit()


def downgrade() -> None:
    session = Session(bind=op.get_bind())
    statement = delete(Test).where(Test.description.in_(tests))
    session.execute(statement)
    session.commit()
