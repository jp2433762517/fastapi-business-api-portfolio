from abc import ABC, abstractmethod
from typing import Dict
from app.application.models.user_dto import LoginRequest, UserResponse, UpdateUserRequest


class UseCase(ABC):
    @abstractmethod
    async def execute(self, request):
        pass


class LoginUserUseCase(UseCase):
    async def execute(self, request: LoginRequest) -> Dict[str, str]:
        # Implementation will be in concrete class
        pass


class GetUserUseCase(UseCase):
    async def execute(self, user_id: int) -> UserResponse:
        pass


class UpdateUserUseCase(UseCase):
    async def execute(self, user_id: int, request: UpdateUserRequest) -> UserResponse:
        pass


class DeleteUserUseCase(UseCase):
    async def execute(self, user_id: int) -> None:
        pass
