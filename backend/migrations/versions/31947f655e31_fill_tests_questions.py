"""Fill tests_questions

Revision ID: 31947f655e31
Revises: 2a7dad98a6d4

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import delete, insert
from sqlalchemy.orm import Session

from models.TestQuestion import TestQuestion

# revision identifiers, used by Alembic.
revision: str = '31947f655e31'
down_revision: Union[str, None] = '2a7dad98a6d4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

tests_questions = [
    {'test_id': 1, 'question_id': 1, 'question_number': 1},
    {'test_id': 1, 'question_id': 5, 'question_number': 2},
    {'test_id': 1, 'question_id': 9, 'question_number': 3},
    {'test_id': 1, 'question_id': 13, 'question_number': 4},
    {'test_id': 1, 'question_id': 17, 'question_number': 5},
    {'test_id': 1, 'question_id': 21, 'question_number': 6},
    {'test_id': 2, 'question_id': 2, 'question_number': 1},
    {'test_id': 2, 'question_id': 6, 'question_number': 2},
    {'test_id': 2, 'question_id': 10, 'question_number': 3},
    {'test_id': 2, 'question_id': 14, 'question_number': 4},
    {'test_id': 2, 'question_id': 18, 'question_number': 5},
    {'test_id': 2, 'question_id': 22, 'question_number': 6},
    {'test_id': 3, 'question_id': 3, 'question_number': 1},
    {'test_id': 3, 'question_id': 7, 'question_number': 2},
    {'test_id': 3, 'question_id': 11, 'question_number': 3},
    {'test_id': 3, 'question_id': 15, 'question_number': 4},
    {'test_id': 3, 'question_id': 19, 'question_number': 5},
    {'test_id': 3, 'question_id': 23, 'question_number': 6},
    {'test_id': 4, 'question_id': 4, 'question_number': 1},
    {'test_id': 4, 'question_id': 8, 'question_number': 2},
    {'test_id': 4, 'question_id': 12, 'question_number': 3},
    {'test_id': 4, 'question_id': 16, 'question_number': 4},
    {'test_id': 4, 'question_id': 20, 'question_number': 5},
    {'test_id': 4, 'question_id': 24, 'question_number': 6},
]


def upgrade() -> None:
    session = Session(bind=op.get_bind())
    session.execute(insert(TestQuestion), tests_questions,)
    session.commit()


def downgrade() -> None:
    session = Session(bind=op.get_bind())
    for test_question in tests_questions:
        statement = delete(TestQuestion).where(
            TestQuestion.test_id == test_question['test_id'],
            TestQuestion.question_id == test_question['question_id'],
            TestQuestion.question_number == test_question['question_number']
        )
        session.execute(statement)
    session.commit()
