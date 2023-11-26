from typing import Optional

from src.api.v1.schemas import BaseResponseSchema


class TextbookResponseSchema(BaseResponseSchema):
    id: int
    school_class: int
    title: str
    slug: Optional[str]
