from typing import List, Tuple

from fastapi import APIRouter


def get_routers() -> List[APIRouter]:
    from src.api.v1.views import user_router, textbook_router, test_router, auth_router

    routers: List[APIRouter] = [
        user_router,
        textbook_router,
        test_router,
        auth_router,
    ]

    return routers
