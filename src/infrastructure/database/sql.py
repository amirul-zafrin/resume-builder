from .config import SessionFactory

def get_session():
    print("creating session")
    session = SessionFactory()
    try:
        print("session created")
        yield session
    except Exception as e:
        print(e)
        session.rollback()
        raise
    finally:
        session.close()
