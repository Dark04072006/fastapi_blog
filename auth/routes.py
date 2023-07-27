from fastapi import APIRouter

from auth import fastapi_users
from auth.auth_backend import backend
from auth.schemas import UserRead, UserCreate, UserUpdate

router = APIRouter()


router.include_router(
    fastapi_users.get_auth_router(backend), prefix="/auth/jwt", tags=["auth"]
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)