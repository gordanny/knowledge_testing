from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import BOOLEAN, VARCHAR

from helper import Base


class User(Base):
    __tablename__ = 'users'
    username = Column(VARCHAR, primary_key=True)
    password = Column(VARCHAR, nullable=False)
    fio = Column(VARCHAR, nullable=False)
    is_admin = Column(BOOLEAN, nullable=False)
