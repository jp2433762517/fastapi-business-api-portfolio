from abc import ABC, abstractmethod
from app.application.use_cases.request.login_request import LoginRequest
from app.application.use_cases.request.update_user_request import UpdateUserRequest
from app.application.use_cases.response.user_response import UserResponse


class IUserService(ABC):
    @abstractmethod
    async def login(self, request: LoginRequest) -> dict:
        pass

    @abstractmethod
    async def get_user(self, user_id: int) -> UserResponse:
        pass

    @abstractmethod
    async def update_user(self, user_id: int, request: UpdateUserRequest) -> UserResponse:
        pass

    @abstractmethod
    async def delete_user(self, user_id: int) -> None:
        pass
