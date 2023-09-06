from schemas.base import BaseFromOrmModel
from schemas.question import TestQuestion


class TestBase(BaseFromOrmModel):
    id: int
    description: str
    questions: list[TestQuestion] | None
