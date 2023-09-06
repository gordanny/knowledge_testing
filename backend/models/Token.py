from sqlalchemy import Column, text, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID, VARCHAR

from helper import Base
from models.User import User


class Token(Base):
    __tablename__ = 'tokens'
    token = Column(UUID(as_uuid=False), primary_key=True, server_default=text("uuid_generate_v4()"))
    expires = Column(DateTime(), nullable=False)
    user_id = Column(VARCHAR, ForeignKey(User.username))
