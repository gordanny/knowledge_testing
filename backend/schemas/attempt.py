from pydantic import Field

from schemas.base import BaseFromOrmModel
from schemas.result import ResultBase


class AttemptCreateRequest(BaseFromOrmModel):
    username: str
    test_id: int = Field(validation_alias='testId')
    user_answers: list[ResultBase] = Field(validation_alias='userAnswers')


class AttemptCreate(BaseFromOrmModel):
    username: str
    test_id: int
    right_answers_percent: int
