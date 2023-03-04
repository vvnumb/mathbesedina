from typing import Optional, List
from fastapi import APIRouter, Query

from src.repositories.textbook import TextbookRepository
from src.schemas import TextbookResponseSchema
from src.use_cases.get_textbooks import GetTextbooksCase

router = APIRouter(prefix="/textbooks", tags=["textbooks"])


@router.get("/")
def get_textbooks(
    school_class: Optional[int] = Query(default=None)
) -> List[TextbookResponseSchema]:
    """Получение учебников. Возможен фильтр по классу"""
    resources = dict(
        textbook_repo=TextbookRepository
    )
    get_textbooks_case = GetTextbooksCase(**resources)
    return get_textbooks_case(school_class)
