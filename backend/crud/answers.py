from db.db_conf import database
from models.Answer import Answer


def get_right_answers(answers_ids: list[int] | None = None):
    with database.get_session() as session:
        query = session.query(Answer).filter(Answer.is_right)

        if answers_ids:
            query = query.filter(Answer.id.in_(answers_ids))

        return query.all()
