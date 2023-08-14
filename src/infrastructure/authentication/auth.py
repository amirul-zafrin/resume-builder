from fastapi.security import OAuth2PasswordBearer

from settings import token_url

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=token_url)
