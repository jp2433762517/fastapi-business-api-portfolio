from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class CorporateRequest(BaseModel):
    code: str
    name: str


class CorporateResponse(BaseModel):
    id: int
    code: str
    name: str
    is_active: bool


@router.post("/", response_model=CorporateResponse)
async def create_corporate(request: CorporateRequest):
    # Implement
    return CorporateResponse(id=1, code=request.code, name=request.name, is_active=True)


@router.get("/{corporate_id}", response_model=CorporateResponse)
async def get_corporate(corporate_id: int):
    # Implement
    return CorporateResponse(id=corporate_id, code="code", name="name", is_active=True)
