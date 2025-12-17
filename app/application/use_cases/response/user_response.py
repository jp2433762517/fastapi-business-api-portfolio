from pydantic import BaseModel


class UserResponse(BaseModel):
    id: int
    email: str
    full_name: str
    is_active: bool
    created_at: str
    updated_at: str
