from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker

from settings import database, drivername

conn_str = URL.create(
    drivername=drivername,
    database=database,
)
engine = create_engine(url=conn_str)
SessionFactory = sessionmaker(bind=engine)
