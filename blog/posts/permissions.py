from fastapi import HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from auth import current_active_user
from core.database.config import get_async_session
from core.database.models import User
from .service import get_post

from typing import Optional


async def only_owner_or_superuser_perm(
        post_id: int,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_active_user)
) -> Optional[HTTPException]:
    post = await get_post(session, post_id)
    if post is not None:
        if not post.owner_id == user.id and not user.is_superuser:
            raise HTTPException(403, 'Only the owner can edit/delete this post')
    else:
        raise HTTPException(404, 'post does not exists')
