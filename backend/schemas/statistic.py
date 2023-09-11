from pydantic import field_validator, Field, BaseModel

from schemas.base import BaseFromOrmModel


class QuestionAnswersCounters(BaseFromOrmModel):
    question_number: int = Field(serialization_alias='questionNumber')
    right_answers: int | None = Field(serialization_alias='rightAnswers')
    wrong_answers: int | None = Field(serialization_alias='wrongAnswers')

    @field_validator('wrong_answers', 'right_answers')
    @classmethod
    def replace_none_by_zero(cls, v: int | None) -> int:
        if v is None:
            return 0
        return v


class StatisticsRequest(BaseModel):
    test_id: int = Field(validation_alias='testId')


class StatisticsResponse(BaseModel):
    participants_qty: int = Field(serialization_alias='participantsQty')
    answers_stats: list[QuestionAnswersCounters] = Field(serialization_alias='answersStats')
