from pydantic import BaseModel

class ApiLink(BaseModel):
    href: str
