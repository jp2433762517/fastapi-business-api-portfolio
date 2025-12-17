from typing import Optional, Dict
from app.domain.entities.user import User
from app.domain.value_objects.email import Email
from app.domain.repositories.user_repository import UserRepository


class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.users: Dict[int, User] = {}
        self.email_to_id: Dict[str, int] = {}
        self.next_id = 1

    async def get_by_id(self, user_id: int) -> Optional[User]:
        return self.users.get(user_id)

    async def get_by_email(self, email: Email) -> Optional[User]:
        user_id = self.email_to_id.get(str(email))
        return self.users.get(user_id) if user_id else None

    async def create(self, user: User) -> User:
        user.id = self.next_id
        self.users[user.id] = user
        self.email_to_id[str(user.email)] = user.id
        self.next_id += 1
        return user

    async def update(self, user: User) -> User:
        if user.id in self.users:
            self.users[user.id] = user
            self.email_to_id[str(user.email)] = user.id
        return user

    async def delete(self, user_id: int) -> None:
        user = self.users.pop(user_id, None)
        if user:
            del self.email_to_id[str(user.email)]
