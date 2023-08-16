from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

from settings import token_url, pwd_hash_algo

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=token_url)
crypt_context = CryptContext(schemes=[pwd_hash_algo])
