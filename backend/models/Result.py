from sqlalchemy import Column, ForeignKey, Index
from sqlalchemy.dialects.postgresql import BIGINT, VARCHAR

from helper import Base
from models.Answer import Answer
from models.Attempt import Attempt
from models.TestQuestion import TestQuestion


class Result(Base):
    __tablename__ = 'results'
    id = Column(BIGINT, autoincrement=True, primary_key=True)
    attempt_id = Column(BIGINT, ForeignKey(Attempt.id))
    user_answer_id = Column(BIGINT, ForeignKey(Answer.id))
    __table_args__ = (
        Index('unique_attempt_answer', attempt_id, user_answer_id, unique=True),
    )
