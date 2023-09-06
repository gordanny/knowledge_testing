from pydantic import Field, BaseModel

from schemas.base import BaseFromOrmModel


class ResultBase(BaseFromOrmModel):
    test_question_id: int = Field(validation_alias='questionId')
    user_answer_id: int = Field(validation_alias='answerId')


class ResultCreate(BaseFromOrmModel):
    test_question_id: int
    user_answer_id: int
    attempt_id: int


class ResultRead(ResultCreate):
    id: int


class ResultResponse(BaseModel):
    is_success: bool = Field(serialization_alias='isSuccess')
    percent: int
