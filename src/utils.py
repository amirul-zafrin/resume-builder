from domain.entity import Base
from infrastructure.database.config import engine


def startup_event():
    print("creating db")
    Base.metadata.create_all(bind=engine)
    print("db created")
