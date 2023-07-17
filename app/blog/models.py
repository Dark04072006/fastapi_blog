from sqlalchemy import Column, Integer, String, Text
from app.core.database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(String(500), nullable=False)

    def __repr__(self):
        return f"Post(id={self.id}, title={self.title})"


posts = Post.__table__
