from fastapi import APIRouter

from .user_router import graphql_user_router

v1_router = APIRouter(prefix="/v1")

v1_router.include_router(graphql_user_router, prefix="/user")
