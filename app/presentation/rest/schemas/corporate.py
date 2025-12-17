from pydantic import BaseModel


class CorporateRequest(BaseModel):
    code: str
    name: str


class CorporateResponse(BaseModel):
    id: int
    code: str
    name: str
    is_active: bool
