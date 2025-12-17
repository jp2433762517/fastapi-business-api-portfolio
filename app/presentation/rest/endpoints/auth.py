from fastapi import APIRouter, Depends, HTTPException, status
from app.presentation.rest.schemas.auth import LoginRequest, Token, UserResponse, UpdateUserRequest
from app.presentation.rest.dependencies.auth_dependency import (
    get_user_service, get_current_user
)
from app.application.services.user_service import IUserService
from app.domain.errors import InvalidCredentialsError, UserNotFoundError

router = APIRouter()


@router.post("/login", response_model=Token)
async def login(
    request: LoginRequest,
    service: IUserService = Depends(get_user_service)
):
    try:
        return await service.login(request)
    except InvalidCredentialsError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))


@router.get("/me", response_model=UserResponse)
async def get_user(
    current_user: int = Depends(get_current_user),
    service: IUserService = Depends(get_user_service)
):
    try:
        return await service.get_user(current_user)
    except UserNotFoundError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


@router.put("/me", response_model=UserResponse)
async def update_user(
    request: UpdateUserRequest,
    current_user: int = Depends(get_current_user),
    service: IUserService = Depends(get_user_service)
):
    try:
        return await service.update_user(current_user, request)
    except UserNotFoundError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


@router.delete("/me")
async def delete_user(
    current_user: int = Depends(get_current_user),
    service: IUserService = Depends(get_user_service)
):
    try:
        await service.delete_user(current_user)
        return {"message": "User deleted successfully"}
    except UserNotFoundError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
