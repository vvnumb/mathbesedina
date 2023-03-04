from typing import List, Tuple

from fastapi import APIRouter


def get_routers() -> List[APIRouter]:
    # todo: test
    from starlette.requests import Request
    # from config.asgi import application
    router_v1 = APIRouter(prefix="", tags=["test"])

    @router_v1.get("/app")
    def read_main(request: Request):
        return {"message": "Hello World", "root_path": request.scope.get("root_path")}

    from src.api import user_router, textbook_router

    routers: List[APIRouter] = [
        router_v1,
        user_router,
        textbook_router
    ]

    return routers
