from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, declarative_mixin, mapped_column


@declarative_mixin
class PostsAndCommentsModelMixin:
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    text: Mapped[str] = mapped_column(String(500))
    owner_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
