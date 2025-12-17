from dataclasses import dataclass
from typing import Optional


@dataclass
class DomainEvent:
    pass


@dataclass
class UserCreatedEvent(DomainEvent):
    user_id: int
    email: str
    full_name: str


@dataclass
class UserUpdatedEvent(DomainEvent):
    user_id: int
    old_full_name: str
    new_full_name: str


@dataclass
class UserDeletedEvent(DomainEvent):
    user_id: int
