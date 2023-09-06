from sqlalchemy import insert

from db.db_conf import database
from models.Result import Result
from schemas.result import ResultCreate


def create_results(results: list[ResultCreate]):
    with database.get_session() as session:
        session.execute(insert(Result), results, )
        session.commit()
