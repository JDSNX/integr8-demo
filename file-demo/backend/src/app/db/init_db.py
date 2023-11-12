from db.session import sessionlocal


def get_db():
    db = sessionlocal()
    try:
        yield db
    except:
        db.rollback()
    finally:
        db.close()
