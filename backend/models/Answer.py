from sqlalchemy import Column, ForeignKey, Index
from sqlalchemy.dialects.postgresql import BIGINT, VARCHAR, BOOLEAN

from helper import Base
from models.Question import Question


class Answer(Base):
    __tablename__ = 'answers'
    id = Column(BIGINT, autoincrement=True, primary_key=True)
    text = Column(VARCHAR, nullable=False)
    question_id = Column(BIGINT, ForeignKey(Question.id))
    is_right = Column(BOOLEAN, nullable=False)
    __table_args__ = (
        Index('unique_question_answer', text, question_id, unique=True),
    )
