from pydantic import BaseModel


class BaseCommentSchema(BaseModel):
    title: str
    text: str


class CommentCreateSchema(BaseCommentSchema):
    post_id: int


class CommentUpdateSchema(BaseCommentSchema):
    pass


class CommentReadSchema(CommentCreateSchema):
    id: int
    owner_id: int

    class Config:
        from_attributes = True
