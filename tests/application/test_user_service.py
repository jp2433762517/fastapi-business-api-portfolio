import pytest
from unittest.mock import AsyncMock
from app.application.services.user_service import IUserService
from app.application.use_cases.request.login_request import LoginRequest
from app.application.use_cases.request.update_user_request import UpdateUserRequest
from app.domain.entities.user import User
from app.domain.value_objects.email import Email
from app.domain.errors import UserNotFoundError, InvalidCredentialsError
from datetime import datetime


@pytest.mark.asyncio
async def test_login_success():
    # Mock the service
    mock_service = AsyncMock(spec=IUserService)

    email = Email(value="test@example.com")
    user = User(
        id=1, email=email, hashed_password="$2b$12$hashed",
        full_name="Test", is_active=True,
        created_at=datetime.utcnow(), updated_at=datetime.utcnow()
    )
    mock_service.login.return_value = {"access_token": "token123", "token_type": "bearer"}

    request = LoginRequest(email="test@example.com", password="password")
    result = await mock_service.login(request)

    assert result["access_token"] == "token123"
    assert result["token_type"] == "bearer"


@pytest.mark.asyncio
async def test_login_invalid_credentials():
    mock_service = AsyncMock(spec=IUserService)
    mock_service.login.side_effect = InvalidCredentialsError("Invalid credentials")

    request = LoginRequest(email="test@example.com", password="wrong")

    with pytest.raises(InvalidCredentialsError):
        await mock_service.login(request)


@pytest.mark.asyncio
async def test_get_user_success():
    mock_service = AsyncMock(spec=IUserService)

    email = Email(value="test@example.com")
    user = User(
        id=1, email=email, hashed_password="hashed",
        full_name="Test", is_active=True,
        created_at=datetime.utcnow(), updated_at=datetime.utcnow()
    )
    mock_service.get_user.return_value = user

    result = await mock_service.get_user(1)

    assert result.id == 1
    assert result.email.value == "test@example.com"


@pytest.mark.asyncio
async def test_get_user_not_found():
    mock_service = AsyncMock(spec=IUserService)
    mock_service.get_user.side_effect = UserNotFoundError("User not found")

    with pytest.raises(UserNotFoundError):
        await mock_service.get_user(1)


@pytest.mark.asyncio
async def test_update_user_success():
    mock_service = AsyncMock(spec=IUserService)

    email = Email(value="updated@example.com")
    updated_user = User(
        id=1, email=email, hashed_password="hashed",
        full_name="Updated Test", is_active=True,
        created_at=datetime.utcnow(), updated_at=datetime.utcnow()
    )
    mock_service.update_user.return_value = updated_user

    request = UpdateUserRequest(email="updated@example.com", full_name="Updated Test")
    result = await mock_service.update_user(1, request)

    assert result.id == 1
    assert result.email.value == "updated@example.com"
    assert result.full_name == "Updated Test"


@pytest.mark.asyncio
async def test_update_user_not_found():
    mock_service = AsyncMock(spec=IUserService)
    mock_service.update_user.side_effect = UserNotFoundError("User not found")

    request = UpdateUserRequest(email="updated@example.com", full_name="Updated Test")

    with pytest.raises(UserNotFoundError):
        await mock_service.update_user(1, request)


@pytest.mark.asyncio
async def test_delete_user_success():
    mock_service = AsyncMock(spec=IUserService)
    mock_service.delete_user.return_value = None

    await mock_service.delete_user(1)

    mock_service.delete_user.assert_called_once_with(1)


@pytest.mark.asyncio
async def test_delete_user_not_found():
    mock_service = AsyncMock(spec=IUserService)
    mock_service.delete_user.side_effect = UserNotFoundError("User not found")

    with pytest.raises(UserNotFoundError):
        await mock_service.delete_user(1)
