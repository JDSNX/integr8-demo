from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from db.init_db import get_db
from schemas.posts import PostResponse
from routes.endpoints.deps import extract_json, transform_json, store_json
from core.config import get_settings

settings = get_settings()

router = APIRouter()


@router.post(
    "/api/etl",
    response_model=list[PostResponse],
    response_model_by_alias=False,
)
async def etl_post(db: Session = Depends(get_db)):
    """
    Fetch data from given `MOCK_API_ENDPOINT` \n
    Transform fetched data, add `summary` field to each object \n
    Store each value in list to SQLite
    """

    data = extract_json()
    transformed_json = transform_json(data)

    if not transformed_json:
        raise HTTPException(
            detail="List is empty.", status_code=status.HTTP_400_BAD_REQUEST
        )

    posts = store_json(db=db, transformed_json=transformed_json)

    if not posts:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE)

    return posts
