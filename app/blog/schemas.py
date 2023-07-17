from pydantic import BaseModel


class PostBaseSchema(BaseModel):
    title: str
    content: str


class PostInSchema(PostBaseSchema):
    pass


class PostOutSchema(PostBaseSchema):
    id: int
