from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from auth import current_active_user
from core.database.config import get_async_session
from core.database.models import User
from . import services, schemas
from .permissions import only_owner_or_superuser_perm

router = APIRouter(prefix='/comments', tags=['comments'])


@router.get('/', response_model=List[schemas.CommentReadSchema], dependencies={Depends(current_active_user),})
async def get_comments_list_view(session: AsyncSession = Depends(get_async_session)):
    return await services.get_comments(session)


@router.get('/from-post', response_model=List[schemas.CommentReadSchema], dependencies={
    Depends(current_active_user),
})
async def get_comments_from_post_view(post_id: int, session: AsyncSession = Depends(get_async_session)):
    return await services.get_comments_from_cur_post(post_id, session)


@router.post('/', response_model=schemas.CommentReadSchema)
async def create_post_view(comment: schemas.CommentCreateSchema, session: AsyncSession = Depends(get_async_session),
                           user: User = Depends(current_active_user)):
    return await services.add_comment(session, comment.post_id, comment.title, comment.text, user)


@router.patch('/{comment_id}', response_model=schemas.CommentReadSchema, dependencies={Depends(current_active_user), Depends(only_owner_or_superuser_perm)})
async def update_post_view(comment_id: int, comment: schemas.CommentUpdateSchema, session: AsyncSession = Depends(get_async_session)):
    return await services.update_comment(session, comment_id, comment.title, comment.text)


@router.delete('/{comment_id}', dependencies={Depends(current_active_user), Depends(only_owner_or_superuser_perm)})
async def delete_post_view(comment_id: int, session: AsyncSession = Depends(get_async_session)):
    await services.delete_comment(session, comment_id)
    return JSONResponse('post deleted successfully')
