from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import BIGINT, BOOLEAN, VARCHAR

from helper import Base


class Test(Base):
    __tablename__ = 'tests'
    id = Column(BIGINT, autoincrement=True, primary_key=True)
    description = Column(VARCHAR, nullable=False, unique=True)
    success_percent = Column(BIGINT, default=80)
