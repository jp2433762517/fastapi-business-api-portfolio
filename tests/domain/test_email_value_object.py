import pytest
from pydantic import ValidationError
from app.domain.value_objects.email import Email


def test_email_creation_valid():
    email = Email(value="test@example.com")
    assert email.value == "test@example.com"


def test_email_creation_invalid():
    with pytest.raises(ValidationError):
        Email(value="invalid-email")


def test_email_str():
    email = Email(value="test@example.com")
    assert str(email) == "test@example.com"
