from fastapi import APIRouter

from .v1 import v1_router

graphql_router = APIRouter(prefix="/graphql")

graphql_router.include_router(v1_router)
