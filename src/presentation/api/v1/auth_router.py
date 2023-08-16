from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from application.service import AuthService
from application.model import TokenModel, UserResponseModel, UserPostModel

auth_router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@auth_router.post(
    "/login",
    response_model=TokenModel,
)
async def login_user(
    form_data: OAuth2PasswordRequestForm = Depends(),
    service: AuthService = Depends(),
):
    token = service.login(data=form_data)
    return token


@auth_router.post(
    "/signup",
    response_model=UserResponseModel,
)
async def signup_user(
    data: UserPostModel,
    service: AuthService = Depends(),
):
    created_user = service.signup(data=data)
    return created_user


@auth_router.get("/me")
async def get_my_details(details=Depends(AuthService.validate_user)):
    return details
