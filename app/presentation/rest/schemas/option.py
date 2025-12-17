from pydantic import BaseModel


class OptionRequest(BaseModel):
    name: str
    value: str


class OptionResponse(BaseModel):
    id: int
    name: str
    value: str
