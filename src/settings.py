from os import getenv

from dotenv import load_dotenv

load_dotenv()

# database
drivername = getenv("drivername")
database = getenv("database")
# auth
token_url = getenv("token_url")
pwd_hash_algo = getenv("pwd_hash_algo")
jwt_hash_algo = getenv("jwt_hash_algo")
expiration_minute = int(exp) if (exp := getenv("expiration_minute")) else 15
secret_key = getenv("secret_key")
