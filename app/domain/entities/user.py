from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List

from app.domain.events import DomainEvent, UserCreatedEvent, UserUpdatedEvent, UserDeletedEvent
from app.domain.value_objects.email import Email


@dataclass
class User:
    id: Optional[int]
    email: Email
    hashed_password: str
    full_name: str
    is_active: bool
    created_at: datetime
    updated_at: datetime
    events: List[DomainEvent] = field(default_factory=list)

    @classmethod
    def create(cls, email: Email, hashed_password: str, full_name: str) -> 'User':
        now = datetime.utcnow()
        user = cls(
            id=None,
            email=email,
            hashed_password=hashed_password,
            full_name=full_name,
            is_active=True,
            created_at=now,
            updated_at=now,
            events=[]
        )
        user.events.append(UserCreatedEvent(
            user_id=user.id,
            email=str(user.email),
            full_name=user.full_name
        ))
        return user

    def update_info(self, full_name: str):
        old_name = self.full_name
        self.full_name = full_name
        self.updated_at = datetime.utcnow()
        self.events.append(UserUpdatedEvent(
            user_id=self.id,
            old_full_name=old_name,
            new_full_name=full_name
        ))

    def deactivate(self):
        self.is_active = False
        self.updated_at = datetime.utcnow()
        self.events.append(UserDeletedEvent(user_id=self.id))
