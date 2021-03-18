from app.api.web.abstract_resource import AbstractResource
from pydantic import BaseModel
from typing import Any
from pydantic.fields import Field

from .db_model import DbModel


class UserData(BaseModel):
    firstname: str
    lastname: str
    email: str


class User(UserData, DbModel):
    pass

class UserResource(AbstractResource, UserData):
    pass
