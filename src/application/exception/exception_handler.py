from fastapi import Request, status
from fastapi.responses import JSONResponse
from .error import EntryNotFoundError, UnauthorizedError


async def entry_not_found(request: Request, exc: EntryNotFoundError):
    return JSONResponse(
        {"detail": str(exc)},
        status_code=status.HTTP_404_NOT_FOUND,
    )


async def unauthorized(request: Request, exc: UnauthorizedError):
    return JSONResponse(
        {"detail": str(exc)},
        status_code=status.HTTP_401_UNAUTHORIZED,
    )


exception_handlers = {
    EntryNotFoundError: entry_not_found,
    UnauthorizedError: unauthorized,
}
