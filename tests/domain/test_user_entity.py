import pytest
from datetime import datetime
from app.domain.entities.user import User
from app.domain.value_objects.email import Email


def test_user_creation():
    email = Email(value="test@example.com")
    user = User(
        id=None,
        email=email,
        hashed_password="hashed_pass",
        full_name="Test User",
        is_active=True,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    assert user.email.value == "test@example.com"
    assert user.full_name == "Test User"
    assert user.is_active is True


def test_user_update_info():
    email = Email(value="test@example.com")
    user = User(
        id=1,
        email=email,
        hashed_password="hashed_pass",
        full_name="Test User",
        is_active=True,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    user.update_info("Updated Name")
    assert user.full_name == "Updated Name"
    assert user.updated_at > user.created_at


def test_user_deactivate():
    email = Email(value="test@example.com")
    user = User(
        id=1,
        email=email,
        hashed_password="hashed_pass",
        full_name="Test User",
        is_active=True,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    user.deactivate()
    assert user.is_active is False
