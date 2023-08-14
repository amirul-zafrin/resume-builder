from os import getenv

from dotenv import load_dotenv

load_dotenv()

# database
drivername = getenv("drivername")
database = getenv("database")
# auth
token_url = getenv("token_url")
