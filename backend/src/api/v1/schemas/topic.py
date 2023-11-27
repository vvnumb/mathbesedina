from typing import List, Optional

from src.api.v1.schemas import BaseResponseSchema


class ShortTopicResponseSchema(BaseResponseSchema):
    """Схема для возврата темы в списке"""
    id: int
    title: str
    slug: Optional[str]


class _TopicVideoSchema(BaseResponseSchema):
    """Внутренняя структура видео внутри ответа темы"""
    title: Optional[str]
    link: str
    
class _TopicTestSchema(BaseResponseSchema):
    """Внутренняя структура теста внутри ответа темы"""
    id: int
    title: str


class FullTopicResponseSchema(BaseResponseSchema):
    """Схема для возврата темы в списке"""
    id: int
    title: str
    description: str
    videos: List[_TopicVideoSchema]
    tests: List[_TopicTestSchema]
