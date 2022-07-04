"""Main module."""

import sys

from dependency_injector.wiring import Provide, inject

from .services import UserService, AuthService, PhotoService
from .containers import Application


class MyQuery:
    @staticmethod
    @inject
    def resolve_email(name: str, cupu_service: PhotoService = Provide[Application.services.cupu]):
        cupu_service.hello(name)


@inject
def main(
        email: str,
        password: str,
        photo: str,
        user_service: UserService = Provide[Application.services.user],
        auth_service: AuthService = Provide[Application.services.auth],
        photo_service: PhotoService = Provide[Application.services.photo],
) -> None:
    user = user_service.get_user(email)
    auth_service.authenticate(user, password)
    photo_service.upload_photo(user, photo)
    MyQuery.resolve_email("raka")


if __name__ == "__main__":
    application = Application()
    application.core.init_resources()
    application.wire(modules=[__name__])

    main(*sys.argv[1:])
