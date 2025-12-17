from datetime import datetime
from passlib.context import CryptContext
from app.application.services.user_service import IUserService
from app.application.use_cases.request.login_request import LoginRequest
from app.application.use_cases.request.update_user_request import UpdateUserRequest
from app.application.use_cases.response.user_response import UserResponse
from app.domain.entities.user import User
from app.domain.value_objects.email import Email
from app.domain.errors import UserNotFoundError, InvalidCredentialsError, EmailAlreadyExistsError
from app.domain.repositories.user_repository import UserRepository
from app.infrastructure.services.jwt_service import JWTService
from app.domain.events import DomainEvent

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserServiceImpl(IUserService):
    def __init__(self, user_repo: UserRepository, jwt_service: JWTService):
        self.user_repo = user_repo
        self.jwt_service = jwt_service

    async def login(self, request: LoginRequest) -> dict:
        email = Email(value=request.email)
        user = await self.user_repo.get_by_email(email)
        if not user or not pwd_context.verify(request.password, user.hashed_password):
            raise InvalidCredentialsError("Invalid email or password")
        if not user.is_active:
            raise InvalidCredentialsError("User is not active")
        token = self.jwt_service.create_access_token({"sub": str(user.id)})
        return {"access_token": token, "token_type": "bearer"}

    async def get_user(self, user_id: int) -> UserResponse:
        user = await self.user_repo.get_by_id(user_id)
        if not user:
            raise UserNotFoundError("User not found")
        return UserResponse(
            id=user.id,
            email=str(user.email),
            full_name=user.full_name,
            is_active=user.is_active,
            created_at=user.created_at.isoformat(),
            updated_at=user.updated_at.isoformat()
        )

    async def update_user(self, user_id: int, request: UpdateUserRequest) -> UserResponse:
        user = await self.user_repo.get_by_id(user_id)
        if not user:
            raise UserNotFoundError("User not found")
        user.update_info(request.full_name)
        updated_user = await self.user_repo.update(user)
        # Process domain events
        for event in updated_user.events:
            print(f"Domain Event: {event}")
        # Clear events after processing
        updated_user.events.clear()
        return UserResponse(
            id=updated_user.id,
            email=str(updated_user.email),
            full_name=updated_user.full_name,
            is_active=updated_user.is_active,
            created_at=updated_user.created_at.isoformat(),
            updated_at=updated_user.updated_at.isoformat()
        )

    async def delete_user(self, user_id: int) -> None:
        user = await self.user_repo.get_by_id(user_id)
        if not user:
            raise UserNotFoundError("User not found")
        user.deactivate()
        updated_user = await self.user_repo.update(user)
        # Process domain events
        for event in updated_user.events:
            print(f"Domain Event: {event}")
        # Clear events after processing
        updated_user.events.clear()
