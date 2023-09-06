from pydantic import BaseModel, ConfigDict


class BaseFromOrmModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
