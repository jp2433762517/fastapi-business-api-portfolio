import pytest
from app.infrastructure.services.jwt_service import JWTService


def test_create_access_token():
    service = JWTService()
    data = {"sub": "1"}
    token = service.create_access_token(data)
    assert isinstance(token, str)
    assert len(token) > 0


def test_verify_token_valid():
    service = JWTService()
    data = {"sub": "1"}
    token = service.create_access_token(data)
    user_id = service.verify_token(token)
    assert user_id == 1


def test_verify_token_invalid():
    service = JWTService()
    user_id = service.verify_token("invalid_token")
    assert user_id is None
