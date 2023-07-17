from app.blog.models import posts
from app.core.database import database
from app.blog.schemas import PostInSchema, PostOutSchema

from fastapi.responses import JSONResponse


async def get_post_list() -> list[posts]:
    return await database.fetch_all(query=posts.select())


async def get_single_post(user_id: int) -> PostOutSchema:
    return await database.fetch_one(query=posts.select().where(
        posts.c.id == user_id
    ))


async def create_post(item: PostInSchema) -> PostOutSchema:
    post = posts.insert().values(**item.dict())
    post_id = await database.execute(post)
    result = {'id': post_id, **item.dict()}
    return PostOutSchema(**result)


async def update_post(post_id: int, item: PostInSchema) -> PostOutSchema:
    post = posts.update().where(posts.c.id == post_id).values(
        **item.dict()
    )
    await database.execute(post)
    return await database.fetch_one(query=posts.select().where(
        posts.c.id == post_id
    ))


async def delete_post(post_id: int) -> None:
    await database.execute(posts.delete().where(posts.c.id == post_id))
