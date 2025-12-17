from pydantic import BaseModel, EmailStr, validator


class Email(BaseModel):
    value: EmailStr

    @validator('value', allow_reuse=True)
    def validate_email(cls, v):
        return v.lower()

    def __str__(self):
        return self.value
