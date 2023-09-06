"""Fill answers

Revision ID: 2a7dad98a6d4
Revises: 381e94e0d0c5

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import delete, insert, select
from sqlalchemy.orm import Session

from models.Answer import Answer

# revision identifiers, used by Alembic.
revision: str = '2a7dad98a6d4'
down_revision: Union[str, None] = '381e94e0d0c5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

answers = [
    {
        'text': 'А',
        'question_id': 1,
        'is_right': True,
    },
    {
        'text': 'Б',
        'question_id': 1,
        'is_right': False,
    },
    {
        'text': 'В',
        'question_id': 1,
        'is_right': False,
    },
    {
        'text': 'Г',
        'question_id': 1,
        'is_right': False,
    },
    {
        'text': 'А',
        'question_id': 2,
        'is_right': False,
    },
    {
        'text': 'Б',
        'question_id': 2,
        'is_right': True,
    },
    {
        'text': 'В',
        'question_id': 2,
        'is_right': False,
    },
    {
        'text': 'Г',
        'question_id': 2,
        'is_right': False,
    },
    {
        'text': 'А',
        'question_id': 3,
        'is_right': False,
    },
    {
        'text': 'Б',
        'question_id': 3,
        'is_right': False,
    },
    {
        'text': 'В',
        'question_id': 3,
        'is_right': True,
    },
    {
        'text': 'Г',
        'question_id': 3,
        'is_right': False,
    },
    {
        'text': 'А',
        'question_id': 4,
        'is_right': False,
    },
    {
        'text': 'Б',
        'question_id': 4,
        'is_right': False,
    },
    {
        'text': 'В',
        'question_id': 4,
        'is_right': False,
    },
    {
        'text': 'Г',
        'question_id': 4,
        'is_right': True,
    },
    {
        'text': '2',
        'question_id': 5,
        'is_right': True,
    },
    {
        'text': '4',
        'question_id': 5,
        'is_right': False,
    },
    {
        'text': '6',
        'question_id': 5,
        'is_right': False,
    },
    {
        'text': '8',
        'question_id': 5,
        'is_right': False,
    },
    {
        'text': '2',
        'question_id': 6,
        'is_right': False,
    },
    {
        'text': '4',
        'question_id': 6,
        'is_right': True,
    },
    {
        'text': '6',
        'question_id': 6,
        'is_right': False,
    },
    {
        'text': '8',
        'question_id': 6,
        'is_right': False,
    },
    {
        'text': '2',
        'question_id': 7,
        'is_right': False,
    },
    {
        'text': '4',
        'question_id': 7,
        'is_right': False,
    },
    {
        'text': '6',
        'question_id': 7,
        'is_right': True,
    },
    {
        'text': '8',
        'question_id': 7,
        'is_right': False,
    },
    {
        'text': '2',
        'question_id': 8,
        'is_right': False,
    },
    {
        'text': '4',
        'question_id': 8,
        'is_right': False,
    },
    {
        'text': '6',
        'question_id': 8,
        'is_right': False,
    },
    {
        'text': '8',
        'question_id': 8,
        'is_right': True,
    },
    {
        'text': 'Меркурий',
        'question_id': 9,
        'is_right': True,
    },
    {
        'text': 'Венера',
        'question_id': 9,
        'is_right': False,
    },
    {
        'text': 'Земля',
        'question_id': 9,
        'is_right': False,
    },
    {
        'text': 'Марс',
        'question_id': 9,
        'is_right': False,
    },
    {
        'text': 'Меркурий',
        'question_id': 10,
        'is_right': False,
    },
    {
        'text': 'Венера',
        'question_id': 10,
        'is_right': True,
    },
    {
        'text': 'Земля',
        'question_id': 10,
        'is_right': False,
    },
    {
        'text': 'Марс',
        'question_id': 10,
        'is_right': False,
    },
    {
        'text': 'Меркурий',
        'question_id': 11,
        'is_right': False,
    },
    {
        'text': 'Венера',
        'question_id': 11,
        'is_right': False,
    },
    {
        'text': 'Земля',
        'question_id': 11,
        'is_right': True,
    },
    {
        'text': 'Марс',
        'question_id': 11,
        'is_right': False,
    },
    {
        'text': 'Меркурий',
        'question_id': 12,
        'is_right': False,
    },
    {
        'text': 'Венера',
        'question_id': 12,
        'is_right': False,
    },
    {
        'text': 'Земля',
        'question_id': 12,
        'is_right': False,
    },
    {
        'text': 'Марс',
        'question_id': 12,
        'is_right': True,
    },
    {
        'text': '4',
        'question_id': 13,
        'is_right': True,
    },
    {
        'text': '8',
        'question_id': 13,
        'is_right': False,
    },
    {
        'text': '16',
        'question_id': 13,
        'is_right': False,
    },
    {
        'text': '32',
        'question_id': 13,
        'is_right': False,
    },
    {
        'text': '4',
        'question_id': 14,
        'is_right': False,
    },
    {
        'text': '8',
        'question_id': 14,
        'is_right': True,
    },
    {
        'text': '16',
        'question_id': 14,
        'is_right': False,
    },
    {
        'text': '32',
        'question_id': 14,
        'is_right': False,
    },
    {
        'text': '4',
        'question_id': 15,
        'is_right': False,
    },
    {
        'text': '8',
        'question_id': 15,
        'is_right': False,
    },
    {
        'text': '16',
        'question_id': 15,
        'is_right': True,
    },
    {
        'text': '32',
        'question_id': 15,
        'is_right': False,
    },
    {
        'text': '4',
        'question_id': 16,
        'is_right': False,
    },
    {
        'text': '8',
        'question_id': 16,
        'is_right': False,
    },
    {
        'text': '16',
        'question_id': 16,
        'is_right': False,
    },
    {
        'text': '32',
        'question_id': 16,
        'is_right': True,
    },
    {
        'text': 'Пушкин А.С.',
        'question_id': 17,
        'is_right': True,
    },
    {
        'text': 'Лермонтов М.Ю.',
        'question_id': 17,
        'is_right': False,
    },
    {
        'text': 'Есенин С.А.',
        'question_id': 17,
        'is_right': False,
    },
    {
        'text': 'Маяковский В.В.',
        'question_id': 17,
        'is_right': False,
    },
    {
        'text': 'Пушкин А.С.',
        'question_id': 18,
        'is_right': False,
    },
    {
        'text': 'Лермонтов М.Ю.',
        'question_id': 18,
        'is_right': True,
    },
    {
        'text': 'Есенин С.А.',
        'question_id': 18,
        'is_right': False,
    },
    {
        'text': 'Маяковский В.В.',
        'question_id': 18,
        'is_right': False,
    },
    {
        'text': 'Пушкин А.С.',
        'question_id': 19,
        'is_right': False,
    },
    {
        'text': 'Лермонтов М.Ю.',
        'question_id': 19,
        'is_right': False,
    },
    {
        'text': 'Есенин С.А.',
        'question_id': 19,
        'is_right': True,
    },
    {
        'text': 'Маяковский В.В.',
        'question_id': 19,
        'is_right': False,
    },
    {
        'text': 'Пушкин А.С.',
        'question_id': 20,
        'is_right': False,
    },
    {
        'text': 'Лермонтов М.Ю.',
        'question_id': 20,
        'is_right': False,
    },
    {
        'text': 'Есенин С.А.',
        'question_id': 20,
        'is_right': False,
    },
    {
        'text': 'Маяковский В.В.',
        'question_id': 20,
        'is_right': True,
    },
    {
        'text': '10001',
        'question_id': 21,
        'is_right': True,
    },
    {
        'text': '100001',
        'question_id': 21,
        'is_right': False,
    },
    {
        'text': '110110',
        'question_id': 21,
        'is_right': False,
    },
    {
        'text': '1011000',
        'question_id': 21,
        'is_right': False,
    },
    {
        'text': '10001',
        'question_id': 22,
        'is_right': False,
    },
    {
        'text': '100001',
        'question_id': 22,
        'is_right': True,
    },
    {
        'text': '110110',
        'question_id': 22,
        'is_right': False,
    },
    {
        'text': '1011000',
        'question_id': 22,
        'is_right': False,
    },
    {
        'text': '10001',
        'question_id': 23,
        'is_right': False,
    },
    {
        'text': '100001',
        'question_id': 23,
        'is_right': False,
    },
    {
        'text': '110110',
        'question_id': 23,
        'is_right': True,
    },
    {
        'text': '1011000',
        'question_id': 23,
        'is_right': False,
    },
    {
        'text': '10001',
        'question_id': 24,
        'is_right': False,
    },
    {
        'text': '100001',
        'question_id': 24,
        'is_right': False,
    },
    {
        'text': '110110',
        'question_id': 24,
        'is_right': False,
    },
    {
        'text': '1011000',
        'question_id': 24,
        'is_right': True,
    },
]


def upgrade() -> None:
    session = Session(bind=op.get_bind())
    session.execute(insert(Answer), answers,)
    session.commit()


def downgrade() -> None:
    session = Session(bind=op.get_bind())
    for answer in answers:
        statement = delete(Answer).where(Answer.text == answer['text'], Answer.question_id == answer['question_id'])
        session.execute(statement)
    session.commit()
