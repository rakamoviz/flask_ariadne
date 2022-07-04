from ariadne_graphql_modules import InputType, MutationType, convert_case, gql
from dependency_injector.wiring import Provide, inject
from webserver.services import User as UserService
from webserver.containers import Application as ApplicationContainer

class RegisterUserInput(InputType):
    __schema__ = gql(
        """
        input RegisterUserInput {
            name: String!
            email: String!
        }
        """
    )
    __args__ = convert_case


class RegisterUser(MutationType):
    __schema__ = gql(
        """
        type Mutation {
            registerUser(input: RegisterUserInput!): Boolean!
        }
        """
    )
    __requires__ = [RegisterUserInput]

    @staticmethod
    @inject
    async def resolve_mutation(*_, input: dict, user_service: UserService = Provide[ApplicationContainer.user]):
        user = await user_service.create_user(
            name=input["name"],
            email=input["email"],
        )
        return bool(user)
