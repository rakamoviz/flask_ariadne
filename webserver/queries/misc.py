from datetime import date

from ariadne.asgi import GraphQL
from ariadne_graphql_modules import ObjectType, gql


class Year(ObjectType):
    __schema__ = gql(
        """
        type Query {
            year: Int!
        }
        """
    )

    @staticmethod
    def resolve_year(*_):
        return date.today().year


class Message(ObjectType):
    __schema__ = gql(
        """
        type Query {
            message: String!
        }
        """
    )

    @staticmethod
    def resolve_message(*_):
        return "Hello world!"
