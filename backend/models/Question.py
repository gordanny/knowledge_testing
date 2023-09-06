from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import BIGINT, VARCHAR

from helper import Base


class Question(Base):
    __tablename__ = 'questions'
    id = Column(BIGINT, autoincrement=True, primary_key=True)
    description = Column(VARCHAR, nullable=False, unique=True)
