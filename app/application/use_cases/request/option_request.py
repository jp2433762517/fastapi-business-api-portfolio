from pydantic import BaseModel


class OptionRequest(BaseModel):
    name: str
    value: str
