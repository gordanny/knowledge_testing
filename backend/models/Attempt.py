from datetime import datetime

from sqlalchemy import Column, ForeignKey, Index
from sqlalchemy.dialects.postgresql import BIGINT, TIMESTAMP, VARCHAR

from helper import Base
from models.Test import Test
from models.User import User


class Attempt(Base):
    __tablename__ = 'attempts'
    id = Column(BIGINT, autoincrement=True, primary_key=True)
    username = Column(VARCHAR, ForeignKey(User.username))
    test_id = Column(BIGINT, ForeignKey(Test.id))
    answered_at = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)
    right_answers_percent = Column(BIGINT, nullable=False)
    __table_args__ = (
        Index('unique_user_test_attempt', username, test_id, answered_at, unique=True),
    )
