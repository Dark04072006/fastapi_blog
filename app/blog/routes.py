from app.blog import crud
from fastapi import APIRouter
from app.blog.schemas import PostInSchema, PostOutSchema

router = APIRouter()


@router.get('/', status_code=200, response_model=list[PostOutSchema],
            description='Список постов')
async def get_posts():
    return await crud.get_post_list()


@router.get('/{post_id}', status_code=200, response_model=PostOutSchema)
async def single(user_id: int):
    return await crud.get_single_post(user_id)


@router.post('/', status_code=201, response_model=PostOutSchema)
async def add_post(item: PostInSchema):
    return await crud.create_post(item)


@router.put('/{post_id}', status_code=201, response_model=PostOutSchema)
async def post_update(post_id: int, item: PostInSchema):
    return await crud.update_post(post_id, item)


@router.delete('/{post_id}', status_code=204)
async def delete_post(post_id: int) -> None:
    await crud.delete_post(post_id)
