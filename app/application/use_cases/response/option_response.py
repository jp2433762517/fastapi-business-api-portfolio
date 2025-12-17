from pydantic import BaseModel


class OptionResponse(BaseModel):
    id: int
    name: str
    value: str
