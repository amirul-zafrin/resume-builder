from fastapi import FastAPI
from presentation import api_router

app = FastAPI(
    title="Resume Builder",
    summary="API for Resume Builder",
    # TODO: add exception_handlers
)

app.include_router(api_router)
