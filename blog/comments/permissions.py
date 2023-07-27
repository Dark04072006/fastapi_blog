from typing import Optional

from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from auth import current_active_user
from blog.comments.services import get_current_comment
from core.database.config import get_async_session
from core.database.models import User


async def only_owner_or_superuser_perm(
        comment_id: int,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_active_user)
) -> Optional[HTTPException]:
    comment = await get_current_comment(comment_id, session)
    if comment is not None:
        if not comment.owner_id == user.id and not user.is_superuser:
            raise HTTPException(403, 'Only the owner can edit/delete this comment')
    else:
        raise HTTPException(404, 'post comment not exists')