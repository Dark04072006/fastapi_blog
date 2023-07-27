from typing import List
from sqlalchemy import ForeignKey, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .config import Base
from .mixins import PostsAndCommentsModelMixin


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), index=True, unique=True)
    hashed_password: Mapped[str] = mapped_column(String(100), nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    posts: Mapped[List['Post']] = relationship(back_populates='owner')
    comments: Mapped[List['Comment']] = relationship(back_populates='owner')


class Post(PostsAndCommentsModelMixin, Base):
    __tablename__ = 'post'

    owner: Mapped['User'] = relationship(back_populates='posts')
    comments: Mapped[List['Comment']] = relationship(back_populates='post')


class Comment(PostsAndCommentsModelMixin, Base):
    __tablename__ = 'comment'

    owner: Mapped['User'] = relationship(back_populates='comments')
    post_id: Mapped[int] = mapped_column(ForeignKey('post.id'))
    post: Mapped['Post'] = relationship(back_populates='comments')
