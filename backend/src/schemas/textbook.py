from typing import Optional

from src.schemas import BaseResponseSchema


class TextbookResponseSchema(BaseResponseSchema):
    school_class: int
    title: str
    slug: Optional[str]
