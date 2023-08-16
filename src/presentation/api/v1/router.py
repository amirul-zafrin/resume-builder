from fastapi import APIRouter, Security
from infrastructure.authentication import oauth2_scheme

from .auth_router import auth_router
from .ping_router import ping_router
from .user_router import user_router

v1_router = APIRouter(prefix="/v1")

v1_router.include_router(router=ping_router, dependencies=[Security(oauth2_scheme)])
v1_router.include_router(router=auth_router)
v1_router.include_router(router=user_router)
