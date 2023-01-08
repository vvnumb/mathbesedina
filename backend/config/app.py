import fastapi as FastApi

from config.initializers import initialize_application, initialize_middlewares, initialize_routers


def get_fastapi_application() -> FastApi:
    application: FastApi = initialize_application()
    initialize_routers(application)
    initialize_middlewares(application)
    return application
