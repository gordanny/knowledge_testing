from datetime import datetime, timedelta

from sqlalchemy import insert

from db.db_conf import database
from models.Token import Token
from schemas.token import TokenBase


def create_user_token(username: str):
    with database.get_session() as session:
        results = session.execute(
            insert(Token).values(
                {'expires': datetime.now() + timedelta(weeks=2), 'user_id': username}
            ).returning(Token.token, Token.expires)
        )
        session.commit()

    return [TokenBase.model_validate(result) for result in results][0] if results else None
