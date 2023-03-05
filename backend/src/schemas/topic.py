from typing import Optional

from src.schemas import BaseResponseSchema


class ShortTopicResponseSchema(BaseResponseSchema):
    """Схема для возврата темы в списке"""
    id: int
    title: str
    slug: Optional[str]
