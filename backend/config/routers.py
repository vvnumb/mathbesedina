from typing import List

from fastapi import APIRouter


def get_routers() -> List[APIRouter]:
    # todo: test
    from starlette.requests import Request
    # from config.asgi import application
    router_v1 = APIRouter(prefix="", tags=["test"])

    @router_v1.get("/app")
    def read_main(request: Request):
        return {"message": "Hello World", "root_path": request.scope.get("root_path")}

    routers: List[APIRouter] = [
        router_v1
    ]

    return routers
