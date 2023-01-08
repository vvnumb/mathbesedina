from typing import Type

from fastapi import FastAPI


def initialize_application() -> FastAPI:
    from config import application_config

    application = FastAPI(**application_config.dict())

    return application


def initialize_routers(application: FastAPI) -> None:
    from config.routers import get_routers

    for router in get_routers():
        application.include_router(router, prefix="/api/v1")


def initialize_middlewares(application: FastAPI) -> None:
    from config.middlewares import get_middlewares

    for item in get_middlewares():
        middleware: Type[object] = item[0]
        options = item[1]
        application.add_middleware(middleware, **options)
