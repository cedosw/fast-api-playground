from app.api.web.api_link import ApiLink
from typing import Optional, Any
from pydantic import BaseModel
from pydantic.fields import Field
from bson import ObjectId
from fastapi import Request


class AbstractResource(BaseModel):
    id: Optional[str] = Field(None)
    links: dict[str, ApiLink] = Field(dict(), alias="_links")

    def __init__(self, id: ObjectId, **data: Any) -> None:
        super().__init__(**data)
        self.id = str(id)

    def add_self_link(self, resource_path: str, request: Request):
        self_path = f"{resource_path}/{self.id}"
        self.add_link('self', self_path, request)

    def add_link(self, ref: str, path: str, request: Request):
        self.links[ref] = ApiLink(href = self.build_url(path, request))

    def add_absolute_link(self, ref: str, link: str):
        self.links[ref] = ApiLink(href = link)

    def build_url(self, path: str, request: Request,) -> str:
        return f"{str(request.base_url)}{path[1:]}"
