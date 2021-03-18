from typing import Optional
from pydantic import BaseModel, Field, BaseConfig
from bson import ObjectId
from typing import Any
import logging

class DbModel(BaseModel):
    id: Optional[ObjectId] = Field(None)

    def __init__(self, _id: ObjectId = None, **data: Any) -> None:
        super().__init__(**data)

        if (_id != None):
            self.id = _id

    class Config(BaseConfig):
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: lambda oid: str(oid)
        }