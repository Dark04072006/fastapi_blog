from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

from auth import current_active_user
from blog.posts import service
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from core.database.config import get_async_session
from core.database.models import User
from .schemas import PostGetSchema, BasePostSchema, Message
from .permissions import only_owner_or_superuser_perm

router = APIRouter(prefix='/posts')


@router.get('/', response_model=List[PostGetSchema], dependencies=[Depends(current_active_user)])
async def get_post_list_view(session: AsyncSession = Depends(get_async_session)):
    return await service.get_posts(session)


@router.post('/', response_model=PostGetSchema, responses={403: {'model': Message}})
async def add_post_view(
        post: BasePostSchema,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_active_user)
):
    return await service.add_post(session, post.title, post.text, user)


@router.get('/{post_id}', response_model=PostGetSchema, dependencies=[Depends(current_active_user)],
            responses={404: {'model': Message}, 403: {'model': Message}})
async def get_post_view(post_id: int, session: AsyncSession = Depends(get_async_session)):
    return await service.get_post(session, post_id)


@router.delete('/{post_id}', dependencies={Depends(current_active_user), Depends(only_owner_or_superuser_perm)},
               response_model=Message, responses={202: {'model': Message},
                                                  403: {'model': Message}, 404: {'model': Message}})
async def delete_post_view(post_id: int, session: AsyncSession = Depends(get_async_session)):
    await service.delete_post(session, post_id)
    return JSONResponse(status_code=202, content='post deleted successfully')


@router.patch('/{post_id}', response_model=PostGetSchema, responses={
    404: {'model': Message},
    201: {'model': Message}
}, dependencies={Depends(current_active_user), Depends(only_owner_or_superuser_perm)})
async def update_post_view(post_id: int, post: BasePostSchema, session: AsyncSession = Depends(get_async_session)):
    return await service.update_post(session, post_id, post.title, post.text)
