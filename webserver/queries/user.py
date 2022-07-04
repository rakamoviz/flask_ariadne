from typing import List, Optional

from ariadne.asgi import GraphQL
from ariadne_graphql_modules import DeferredType, ObjectType, gql
from dependency_injector.wiring import Provide, inject
from webserver.services import User as UserService
from webserver.containers import Application as ApplicationContainer
from webserver.models import User as UserModel

class User(ObjectType):
    __schema__ = gql(
        """
        type Query {
            user(id: ID!): User
            users: [User!]!
        }
        """
    )
    __requires__ = [DeferredType("User")]

    @staticmethod
    @inject
    def resolve_user(*_, id: str, user_service: UserService = Provide[ApplicationContainer.user]) -> Optional[UserModel]:
        return user_service.get_user(id=id)

    @staticmethod
    @inject
    def resolve_users(*_, user_service: UserService = Provide[ApplicationContainer.user]) -> List[UserModel]:
        return user_service.get_last_users()


