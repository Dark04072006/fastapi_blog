from pydantic import BaseModel


class BasePostSchema(BaseModel):
    title: str
    text: str


class PostGetSchema(BasePostSchema):
    id: int
    owner_id: int

    class Config:
        from_attributes = True


class Message(BaseModel):
    message: str
