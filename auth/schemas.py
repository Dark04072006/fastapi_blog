from typing import Generic, Optional

from fastapi_users import models
from fastapi_users.schemas import CreateUpdateDictModel, PYDANTIC_V2
from pydantic import EmailStr


class UserRead(CreateUpdateDictModel, Generic[models.ID]):
    """Base User model."""

    id: models.ID
    email: EmailStr
    first_name: str
    last_name: str
    is_active: bool = True
    is_superuser: bool = False

    class Config:
        from_attributes = True


class UserCreate(CreateUpdateDictModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    is_active: bool = True
    is_superuser: bool = False


class UserUpdate(CreateUpdateDictModel):
    password: Optional[str] = None
    email: Optional[EmailStr] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None
