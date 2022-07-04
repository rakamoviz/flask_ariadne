"""Containers module."""

import logging.config

from dependency_injector import containers, providers

from webserver.services import User as UserService

class Application(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(
        packages=["webserver.queries", "webserver.mutations"]
    )

    config = providers.Configuration()

    user = providers.Factory(
        UserService,
    )

    print("?????", user)

