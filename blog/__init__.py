from fastapi import APIRouter

from .posts.routes import router as post_router
from .comments.routes import router as comment_router


def setup_routers() -> APIRouter:
    router = APIRouter()
    router.include_router(post_router, tags=['posts'])
    router.include_router(comment_router, tags=['comments'])
    return router


router = setup_routers()
