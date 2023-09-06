from datetime import datetime

from pydantic import UUID4, Field, field_validator

from schemas.base import BaseFromOrmModel


class TokenBase(BaseFromOrmModel):
    token: UUID4
    expires: datetime
    token_type: str | None = 'bearer'

    @staticmethod
    @field_validator("token")
    def hexlify_token(cls, value):
        return value.hex
