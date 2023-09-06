from pydantic import Field

from schemas.answer import AnswerBase
from schemas.base import BaseFromOrmModel


class QuestionBase(BaseFromOrmModel):
    id: int = Field(validation_alias='question_id')
    description: str


class TestQuestion(QuestionBase):
    question_number: int = Field(serialization_alias='questionNumber')
    answers: list[AnswerBase]
