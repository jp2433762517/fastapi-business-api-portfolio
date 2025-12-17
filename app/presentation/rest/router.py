from fastapi import APIRouter
from app.presentation.rest.endpoints.auth import router as auth_router
from app.presentation.rest.endpoints.corporate import router as corporate_router
from app.presentation.rest.endpoints.option import router as option_router

api_router = APIRouter()
api_router.include_router(auth_router, prefix="/auth", tags=["auth"])
api_router.include_router(corporate_router, prefix="/corporates", tags=["corporates"])
api_router.include_router(option_router, prefix="/options", tags=["options"])
