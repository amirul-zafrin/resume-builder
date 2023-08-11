from fastapi import APIRouter
from .ping_router import ping_router

v1_router = APIRouter(prefix="/v1")

v1_router.include_router(router=ping_router)