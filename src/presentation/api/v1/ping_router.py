from fastapi import APIRouter

ping_router = APIRouter(
    prefix="/ping",
    tags=["Ping - test connection"],
)

@ping_router.get(
    "/",
)
async def ping():
    return "pong"
