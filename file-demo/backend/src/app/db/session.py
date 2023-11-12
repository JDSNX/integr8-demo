from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import Settings

import os

settings = Settings()

file_path = os.path.abspath(os.getcwd()) + "\database.db"


engine = create_engine(
    "sqlite:///" + file_path,
    pool_pre_ping=True,
)

sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
