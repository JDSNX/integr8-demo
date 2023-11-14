import requests
from core.config import get_settings, logger
from schemas.posts import Post, PostUpdate, PostResponse
from models.posts import Post as Post_Model
from sqlalchemy.orm import Session

settings = get_settings()


def extract_json(URL: str = settings.MOCK_API_ENDPOINT) -> list[Post]:
    try:
        mock_json = requests.get(f"{URL}/{settings.DEFAULT_RESOURCE}")
    except requests.exceptions.HTTPError as errh:
        logger.error(f"Extracting process HTTP Error | {errrt}")
    except requests.exceptions.Timeout as errrt:
        logger.error(f"Extracing process time-out | {errrt}")
        raise TimeoutError(errrt)
    else:
        logger.info("Extracting JSON")
        return mock_json.json()


def transform_json(obj_in: list[Post]) -> list[PostUpdate]:
    logger.info("Transforming JSON")
    _updated_obj = [{**data, "summary": data["body"][:50]} for data in obj_in]
    return [PostUpdate(**obj) for obj in _updated_obj]


def store_json(
    db: Session, *, transformed_json: list[PostUpdate]
) -> list[PostResponse]:
    posts = []
    for obj in transformed_json:
        post = Post_Model(**obj.model_dump())
        db.add(post)
        db.commit()
        db.refresh(post)
        posts.append(post)
    logger.info("Storing JSON to SQLite")
    return posts
