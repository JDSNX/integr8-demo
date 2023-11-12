from typing import Optional
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    MOCK_API_ENDPOINT: Optional[str] = None
    SQLALCHEMY_DB_URL: Optional[str] = None
    DEFAULT_RESOURCE: Optional[str] = None

    model_config = SettingsConfigDict(env_file="../../../../.env")


@lru_cache
def get_settings():
    return Settings()
