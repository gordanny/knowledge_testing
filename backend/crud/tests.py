from sqlalchemy import func, literal_column, asc

from db.db_conf import database
from models.Answer import Answer
from models.Question import Question
from models.Test import Test
from models.TestQuestion import TestQuestion
from schemas.test import TestBase


def read_tests():
    with database.get_session() as session:
        answers_query = session.query(
            Answer.question_id,
            func.json_agg(literal_column(Answer.__tablename__)).label('answers')
        ).group_by(Answer.question_id).cte('answers')
        questions_query = session.query(
            Test.id,
            Question.description,
            TestQuestion.id.label('question_id'),
            TestQuestion.question_number,
            answers_query.c.answers
        ) \
            .join(TestQuestion, TestQuestion.test_id == Test.id) \
            .join(Question, Question.id == TestQuestion.question_id) \
            .join(answers_query, answers_query.c.question_id == TestQuestion.question_id) \
            .cte('questions')
        tests_query = session.query(
            Test.id.label('id'),
            Test.description.label('description'),
            func.json_agg(literal_column('questions')).label('questions')
        ).join(questions_query, questions_query.c.id == Test.id).group_by(Test.id).order_by(asc(Test.id))
        result = tests_query.all()

        return [TestBase.model_validate(test) for test in result]


def read_test_success_percent(test_id: int):
    with database.get_session() as session:
        query = session.query(Test.success_percent).filter(Test.id == test_id).all()

        return query[0][0] if query else None
