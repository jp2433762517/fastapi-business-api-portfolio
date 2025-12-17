from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.infrastructure.services.jwt_service import JWTService
from app.domain.repositories.user_repository import UserRepository
from app.infrastructure.repositories.in_memory_user_repository import InMemoryUserRepository
from app.application.services.user_service import IUserService
from app.infrastructure.services.user_service_impl import UserServiceImpl

security = HTTPBearer()


def get_jwt_service() -> JWTService:
    return JWTService()


def get_user_repository() -> UserRepository:
    return InMemoryUserRepository()


def get_user_service(
    user_repo: UserRepository = Depends(get_user_repository),
    jwt_service: JWTService = Depends(get_jwt_service)
) -> IUserService:
    return UserServiceImpl(user_repo, jwt_service)


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    jwt_service: JWTService = Depends(get_jwt_service),
    user_repo: UserRepository = Depends(get_user_repository)
) -> int:
    token = credentials.credentials
    user_id = jwt_service.verify_token(token)
    if user_id is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    user = await user_repo.get_by_id(user_id)
    if not user or not user.is_active:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found or inactive")
    return user_id
