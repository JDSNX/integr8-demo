from sqlalchemy import Column, Integer, String
from db.base import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    post_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    body = Column(String, nullable=False)
    summary = Column(String, nullable=False)
