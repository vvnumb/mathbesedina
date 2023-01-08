from typing import Any, Type
from fastapi.middleware.cors import CORSMiddleware


def get_middlewares() -> list[tuple[Type[object], dict[str, Any]]]:
    from config import cors_config

    middlewares = [
        (CORSMiddleware, cors_config.dict()),
    ]
    return middlewares
