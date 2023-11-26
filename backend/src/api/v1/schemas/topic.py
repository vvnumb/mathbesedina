from typing import List, Optional

from src.api.v1.schemas import BaseResponseSchema


class ShortTopicResponseSchema(BaseResponseSchema):
    """Схема для возврата темы в списке"""
    id: int
    title: str
    slug: Optional[str]


class _TopicVideoSchema(BaseResponseSchema):
    title: Optional[str]
    link: str


class FullTopicResponseSchema(BaseResponseSchema):
    """Схема для возврата темы в списке"""
    id: int
    title: str
    description: str
    slug: Optional[str]
    videos: List[_TopicVideoSchema]
