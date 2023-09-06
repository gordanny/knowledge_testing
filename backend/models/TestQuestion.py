from sqlalchemy import Column, ForeignKey, Index
from sqlalchemy.dialects.postgresql import BIGINT

from helper import Base
from models.Question import Question
from models.Test import Test


class TestQuestion(Base):
    __tablename__ = 'tests_questions'
    id = Column(BIGINT, autoincrement=True, primary_key=True)
    test_id = Column(BIGINT, ForeignKey(Test.id))
    question_id = Column(BIGINT, ForeignKey(Question.id))
    question_number = Column(BIGINT, nullable=False)
    __table_args__ = (
        Index('unique_test_question', test_id, question_id, unique=True),
        Index('unique_test_question_number', test_id, question_number, unique=True),
    )
