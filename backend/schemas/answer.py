from pydantic import Field

from schemas.base import BaseFromOrmModel


class AnswerBase(BaseFromOrmModel):
    id: int
    text: str
    question_id: int = Field(serialization_alias='questionId')
