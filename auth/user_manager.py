from typing import Optional

from fastapi import Depends
from fastapi.requests import Request
from fastapi_users import BaseUserManager, IntegerIDMixin

from auth.utils import get_user_db
from core.database.models import User
from core.settings import SECRET_KEY


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = SECRET_KEY
    verification_token_secret = SECRET_KEY

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
