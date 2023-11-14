import requests
from core.config import get_settings
from schemas.posts import Post, PostUpdate, PostResponse
from models.posts import Post as Post_Model
from sqlalchemy.orm import Session

settings = get_settings()


def extract_json(URL: str = settings.MOCK_API_ENDPOINT) -> list[Post]:
    try:
        mock_json = requests.get(f"{URL}/{settings.DEFAULT_RESOURCE}")
    except requests.exceptions.HTTPError as errh:
        raise SystemExit(errh)
    except requests.exceptions.Timeout as errrt:
        raise TimeoutError(errrt)
    else:
        return mock_json.json()


def transform_json(obj_in: list[Post]) -> list[PostUpdate]:
    return [PostUpdate({**data, "summary": data["body"][:50]}) for data in obj_in]


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
    return posts
