from typing import Optional, List
from fastapi import APIRouter, Query

from src.repositories.textbook import TextbookRepository, TopicRepository
from src.schemas import TextbookResponseSchema, ShortTopicResponseSchema
from src.use_cases import GetTextbooksCase, GetTopicsCase

router = APIRouter(tags=["Textbooks"])


@router.get("/textbooks")
def get_textbooks(
    school_class: Optional[int] = Query(default=None)
) -> List[TextbookResponseSchema]:
    """Получение учебников. Возможен фильтр по классу"""
    resources = dict(
        textbook_repo=TextbookRepository()
    )
    get_textbooks_case = GetTextbooksCase(**resources)
    return get_textbooks_case(school_class)


@router.get("/topics")
def get_topics(
    textbook_id: int = Query(...)
) -> List[ShortTopicResponseSchema]:
    """Получение списка тем по учебнику"""
    resources = dict(
        topic_repo=TopicRepository()
    )
    get_topics_case = GetTopicsCase(**resources)
    return get_topics_case(textbook_id)
