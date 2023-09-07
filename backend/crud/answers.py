from db.db_conf import database
from models.Answer import Answer
from models.TestQuestion import TestQuestion
from schemas.answer import RightAnswers


def get_right_answers(answers_ids: list[int] | None = None):
    with database.get_session() as session:
        query = session.query(Answer).filter(Answer.is_right)

        if answers_ids:
            query = query.filter(Answer.id.in_(answers_ids))

        return query.all()


def get_right_answers_by_test_id(test_id: int):
    with database.get_session() as session:
        query = session.query(TestQuestion.question_number, Answer.text) \
            .join(Answer, Answer.question_id == TestQuestion.question_id) \
            .filter(Answer.is_right, TestQuestion.test_id == test_id)
        query = query.all()

        return [RightAnswers.model_validate(answer) for answer in query]
