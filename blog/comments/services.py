from typing import List

from fastapi import HTTPException, Depends
from sqlalchemy import select, delete, update, insert
from sqlalchemy.exc import NoResultFound

from auth import current_active_user
from blog.posts.service import get_post
from core.database.models import Comment, User
from sqlalchemy.ext.asyncio import AsyncSession


async def get_comments(session: AsyncSession) -> List[Comment]:
    result = await session.execute(select(Comment))
    return result.scalars().all()


async def get_comments_from_cur_post(post_id: int, session: AsyncSession) -> List[Comment]:
    try:
        result = await session.execute(select(Comment).where(Comment.post_id == post_id))
        return result.scalars().all()
    except NoResultFound:
        raise HTTPException(404, 'post does not exists')


async def get_current_comment(comment_id: int, session: AsyncSession) -> Comment:
    try:
        result = await session.execute(select(Comment).where(Comment.id == comment_id))
        return result.one()[0]
    except NoResultFound:
        raise HTTPException(404, 'post does not exists')


async def add_comment(session: AsyncSession, post_id: int, title: str, text: str, user: User) -> Comment:
    post = await get_post(session, post_id)
    comment = Comment(title=title, text=text, owner=user, post=post)
    session.add(comment)
    await session.commit()
    return comment


async def update_comment(session: AsyncSession, comment_id: int, title: str, text: str) -> Comment:
    try:
        result = await session.execute(update(Comment).where(Comment.id == comment_id).values(
            title=title, text=text
        ).returning(Comment))
        await session.commit()
        return result.one()[0]
    except NoResultFound:
        await session.rollback()
        raise HTTPException(404, 'comment does not exists')


async def delete_comment(session: AsyncSession, comment_id: int) -> None:
    try:
        await session.execute(delete(Comment).where(Comment.id == comment_id))
        await session.commit()
    except NoResultFound:
        await session.rollback()
        raise HTTPException(404, 'comment does not exists')
