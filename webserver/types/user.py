from typing import List, Optional

from ariadne.asgi import GraphQL
from ariadne_graphql_modules import ObjectType, gql, convert_case
from webserver.models import User as UserModel


class User(ObjectType):
    __schema__ = gql(
        """
        type User {
            id: ID!
            name: String!
            email: String
        }
        """
    )

    __aliases__ = convert_case

    @staticmethod
    def resolve_email(user: UserModel, info):
        print("info.context is ", info.context.headers.get("User-Agent", "Guest")) 
        #if info.context["is_admin"]:
        return user.email

