"""User request and response schemas."""

from datetime import datetime

from pydantic import EmailStr, Field, field_validator

from app.dto.base import ORMBaseModel


class UserBase(ORMBaseModel):
    """Shared user fields."""

    email: EmailStr
    username: str = Field(min_length=3, max_length=50, pattern=r"^[a-zA-Z0-9_]+$")

    @field_validator("username")
    @classmethod
    def normalize_username(cls, value: str) -> str:
        """Store usernames in a stable lowercase form."""

        return value.strip().lower()


class UserCreate(UserBase):
    """Create user payload."""

    password: str = Field(min_length=8, max_length=128)


class UserUpdate(ORMBaseModel):
    """Update user payload."""

    email: EmailStr | None = None
    username: str | None = Field(
        default=None, min_length=3, max_length=50, pattern=r"^[a-zA-Z0-9_]+$"
    )
    password: str | None = Field(default=None, min_length=8, max_length=128)
    is_active: bool | None = None

    @field_validator("username")
    @classmethod
    def normalize_username(cls, value: str | None) -> str | None:
        """Store usernames in a stable lowercase form."""

        return None if value is None else value.strip().lower()


class UserRead(UserBase):
    """User response."""

    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime
