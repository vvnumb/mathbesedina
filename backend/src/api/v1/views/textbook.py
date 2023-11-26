from typing import Optional, List
from fastapi import APIRouter, Depends, Query

from common.registry import Registry
from src.api.v1.schemas import TextbookResponseSchema, ShortTopicResponseSchema
from src.api.v1.schemas.topic import FullTopicResponseSchema
from src.use_cases import GetTextbooksCase, GetTopicsCase
from src.use_cases.get_single_topic import GetSingleTopicCase

router = APIRouter(tags=["Textbooks"])


@router.get("/textbooks", response_model=List[TextbookResponseSchema])
def get_textbooks(
    school_class: Optional[int] = Query(default=None),
    get_textbooks_case: GetTextbooksCase = Depends(Registry.get_textbooks_case)
):
    """Получение учебников. Возможен фильтр по классу"""
    return get_textbooks_case(school_class)


@router.get("/topics", response_model=List[ShortTopicResponseSchema])
def get_topics(
    textbook_id: int = Query(...),
    get_topics_case: GetTopicsCase = Depends(Registry.get_topics_case)
):
    """Получение списка тем по учебнику"""
    return get_topics_case(textbook_id)


@router.get("/topic", response_model=FullTopicResponseSchema)
def get_single_topic_info(
        topic_id: int = Query(...),
        get_single_topic_case: GetSingleTopicCase = Depends(Registry.get_single_topic_case)
):
    return get_single_topic_case(topic_id)
