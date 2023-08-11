from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker

conn_str = URL.create(
    drivername="sqlite",
    database="resume_db",
)

engine = create_engine(url=conn_str)
SessionFactory = sessionmaker(bind=engine)

def get_session():
    print("creating session")
    session = SessionFactory()
    try:
        print("session created")
        yield session
    except Exception as e:
        session.rollback()
        raise
    finally:
        session.close()
