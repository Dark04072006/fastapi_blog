from typing import List

from fastapi import HTTPException
from sqlalchemy import select, delete, update
from sqlalchemy.exc import NoResultFound

from core.database.models import Post, User
from sqlalchemy.ext.asyncio import AsyncSession


async def get_posts(session: AsyncSession) -> List[Post]:
    result = await session.execute(select(Post))
    return result.scalars().all()


async def add_post(session: AsyncSession,
                   title: str, text: str, owner: User) -> Post:
    post = Post(title=title, text=text, owner=owner)
    session.add(post)
    await session.commit()
    return post


async def get_post(session: AsyncSession, post_id: int) -> Post:
    try:
        result = await session.execute(select(Post).where(Post.id == post_id))
        return result.one()[0]
    except NoResultFound:
        raise HTTPException(404, 'post does not exists')


async def delete_post(session: AsyncSession, post_id: int):
    try:
        await session.execute(delete(Post).where(Post.id == post_id))
        await session.commit()
    except NoResultFound:
        await session.rollback()
        raise HTTPException(404, 'post does not exists')


async def update_post(
        session: AsyncSession,
        post_id: int, title: str, text: str):
    try:
        post = await session.execute(update(Post).where(Post.id == post_id).values(
            title=title,
            text=text
        ).returning(Post))
        await session.commit()
        return post.one()[0]
    except NoResultFound:
        await session.rollback()
        raise HTTPException(404, 'post_does not exists')
