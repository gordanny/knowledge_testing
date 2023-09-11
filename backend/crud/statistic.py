from sqlalchemy import and_, func

from db.db_conf import database
from models.Answer import Answer
from models.Attempt import Attempt
from models.Result import Result
from models.TestQuestion import TestQuestion
from schemas.statistic import QuestionAnswersCounters


def read_test_answers_stats(test_id):
    with database.get_session() as session:
        attempts_cte = session.query(Attempt.username, func.max(Attempt.answered_at)) \
            .filter(Attempt.test_id == test_id) \
            .group_by(Attempt.username) \
            .cte('attempts_cte')

        attempts_ids = session.query(Attempt.id) \
            .join(attempts_cte,
                  and_(Attempt.username == attempts_cte.c.username, Attempt.answered_at == attempts_cte.c.max)) \
            .cte('attempts_ids')

        right_answers = session.query(TestQuestion.question_number, func.count(Answer.is_right)) \
            .join(Answer, Answer.question_id == TestQuestion.question_id) \
            .join(Result, and_(Answer.id == Result.user_answer_id, Answer.is_right)) \
            .filter(Result.attempt_id.in_(attempts_ids)) \
            .group_by(TestQuestion.question_number).cte('right_answers')

        wrong_answers = session.query(TestQuestion.question_number, func.count(Answer.is_right)) \
            .join(Answer, Answer.question_id == TestQuestion.question_id) \
            .join(Result, and_(Answer.id == Result.user_answer_id, Answer.is_right == False)) \
            .filter(Result.attempt_id.in_(attempts_ids)) \
            .group_by(TestQuestion.question_number).cte('wrong_answers')

        answers_count = session.query(
            TestQuestion.question_number,
            right_answers.c.count.label('right_answers'),
            wrong_answers.c.count.label('wrong_answers')
        ) \
            .filter(TestQuestion.test_id == test_id) \
            .join(right_answers, right_answers.c.question_number == TestQuestion.question_number, full=True) \
            .join(wrong_answers, wrong_answers.c.question_number == TestQuestion.question_number, full=True) \
            .order_by(TestQuestion.question_number.asc())

        answers_count_rows = answers_count.all()
        return [QuestionAnswersCounters.model_validate(row) for row in answers_count_rows]


def read_test_participants_qty(test_id):
    with database.get_session() as session:
        attempts_cte = session.query(Attempt.username, func.max(Attempt.answered_at)) \
            .filter(Attempt.test_id == test_id) \
            .group_by(Attempt.username) \
            .cte('attempts_cte')

        test_stats = session.query(func.count(Attempt.id).label('participants_qty')) \
            .join(attempts_cte,
                  and_(Attempt.username == attempts_cte.c.username, Attempt.answered_at == attempts_cte.c.max))

        participants_qty = test_stats.all()

        return participants_qty[0][0] if participants_qty else None
