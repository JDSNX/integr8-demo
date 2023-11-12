from pydantic import BaseModel, Field
from typing import Optional


class PostBase(BaseModel):
    post_id: int = Field(..., alias="id")
    title: Optional[str] = None
    body: Optional[str] = None
    user_id: int = Field(..., alias="userId")


class PostUpdate(PostBase):
    summary: Optional[str] = None


class Post(PostBase):
    pass


class PostResponse(BaseModel):
    id: int = Field(..., alias="post_id")
    userId: int = Field(..., alias="user_id")
    title: Optional[str] = None
    body: Optional[str] = None
    summary: Optional[str] = None
