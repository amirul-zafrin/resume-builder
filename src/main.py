from fastapi import FastAPI

from application.exception import exception_handlers
from presentation import api_router
from utils import startup_event
from presentation.graphql import graphql_router

app = FastAPI(
    title="Resume Builder",
    summary="API for Resume Builder",
    on_startup=[startup_event],
    exception_handlers=exception_handlers,
)

app.include_router(api_router)
app.include_router(graphql_router, prefix="/hahah")
