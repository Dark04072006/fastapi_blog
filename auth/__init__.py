from fastapi_users import FastAPIUsers

from auth import auth_backend
from auth.user_manager import get_user_manager
from core.database.models import User

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend.backend],
)

current_active_user = fastapi_users.current_user(active=True)
current_superuser = fastapi_users.authenticator.current_user(active=True, superuser=True)
