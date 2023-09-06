"""Fill questions

Revision ID: 11302e94d015
Revises: 23bf9b8ba4f5

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import delete, insert
from sqlalchemy.orm import Session

from models.Question import Question

# revision identifiers, used by Alembic.
revision: str = '11302e94d015'
down_revision: Union[str, None] = '23bf9b8ba4f5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

questions = [
    'Первая буква алфавита',
    'Вторая буква алфавита',
    'Третья буква алфавита',
    'Четвертая буква алфавита',
    '1 + 1',
    '2 + 2',
    '3 + 3',
    '4 + 4',
    'Первая планета солнечной системы',
    'Вторая планета солнечной системы',
    'Третья планета солнечной системы',
    'Четвертая планета солнечной системы',
    '2 в степени 2',
    '2 в степени 3',
    '2 в степени 4',
    '2 в степени 5',
    'Автор стихотворения "Зимнее утро"',
    'Автор стихотворения "Бородино"',
    'Автор стихотворения "Берёза"',
    'Автор стихотворения "Облако в штанах"',
    'Число 17 в двоичной системе исчисления',
    'Число 33 в двоичной системе исчисления',
    'Число 54 в двоичной системе исчисления',
    'Число 88 в двоичной системе исчисления',
]


def upgrade() -> None:
    session = Session(bind=op.get_bind())
    session.execute(insert(Question), [{'description': question} for question in questions],)
    session.commit()


def downgrade() -> None:
    session = Session(bind=op.get_bind())
    statement = delete(Question).where(Question.description.in_(questions))
    session.execute(statement)
    session.commit()
