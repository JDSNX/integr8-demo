from db.session import sessionlocal
from core.config import logger


def get_db():
    db = sessionlocal()
    try:
        yield db
    except:
        logger.error("Rollback DB")
        db.rollback()
    finally:
        logger.info("DB Closing...")
        db.close()
