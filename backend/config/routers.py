from typing import List, Tuple

from fastapi import APIRouter


def get_routers() -> List[APIRouter]:
    from src.api import user_router, textbook_router

    routers: List[APIRouter] = [
        user_router,
        textbook_router
    ]

    return routers
