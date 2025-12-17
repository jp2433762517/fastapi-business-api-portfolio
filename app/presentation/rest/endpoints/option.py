from fastapi import APIRouter, Depends, HTTPException
from app.application.use_cases.request.option_request import OptionRequest
from app.application.use_cases.response.option_response import OptionResponse

router = APIRouter()


@router.post("/", response_model=OptionResponse)
async def create_option(request: OptionRequest):
    # Implement create option
    return OptionResponse(id=1, name=request.name, value=request.value)


@router.get("/{option_id}", response_model=OptionResponse)
async def get_option(option_id: int):
    # Implement get option
    return OptionResponse(id=option_id, name="sample", value="value")


@router.put("/{option_id}", response_model=OptionResponse)
async def update_option(option_id: int, request: OptionRequest):
    # Implement update
    return OptionResponse(id=option_id, name=request.name, value=request.value)


@router.delete("/{option_id}")
async def delete_option(option_id: int):
    # Implement delete
    return {"message": "Deleted"}
