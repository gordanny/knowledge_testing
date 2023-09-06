from sqlalchemy import insert

from db.db_conf import database
from models.Attempt import Attempt
from schemas.attempt import AttemptCreate


def create_attempt(attempt: AttemptCreate):
    with database.get_session() as session:
        instance = Attempt(**attempt.model_dump())
        session.add(instance)
        session.commit()

        return instance.id
