from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker

conn_str = URL.create(
    drivername="sqlite",
    database="resume_db.db",
)
engine = create_engine(url=conn_str)
SessionFactory = sessionmaker(bind=engine)
