import strawberry
from fastapi import Depends
from strawberry.fastapi import GraphQLRouter
from strawberry.types import Info

from application.model.strawberry import User
from application.service import UserService


async def get_context(
    service: UserService = Depends(),
):
    return {UserService: service}


@strawberry.type
class QueryUser:
    @strawberry.field
    def user(self, info: Info, user_id: int) -> User:
        service: UserService = info.context[UserService]
        return service.get_by_id(user_id)

    @strawberry.field
    def users(self, info: Info) -> list[User]:
        service: UserService = info.context[UserService]
        return service.get_all()


schema = strawberry.Schema(QueryUser)
graphql_user_router = GraphQLRouter(schema, context_getter=get_context)
