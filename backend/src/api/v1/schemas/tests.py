from typing import List, Optional

from pydantic import model_validator

from common.orm.models.enums import TaskType
from src.api.v1.schemas import BaseResponseSchema
from src.api.v1.schemas.base import BaseResponseRootSchema


class ShortTestResponseSchema(BaseResponseSchema):
    """Схема для возврата темы в списке"""
    id: int
    title: str
    school_class: int
    

class _TestAnswerShortSchema(BaseResponseSchema):
    id: int
    title: str


class _TestTaskSchema(BaseResponseSchema):
    id: int
    task_type: TaskType
    task_text: str
    image_link: Optional[str]
    answers: List[_TestAnswerShortSchema]
    
    @model_validator(mode="before")
    @classmethod
    def hide_full_answers(cls, data):
        if data.task_type == TaskType.FULL:
            data.answers = []
        return data
    

class FullTestResponseSchema(BaseResponseRootSchema):
    root : List[_TestTaskSchema]


class ReviewedTestSchema(BaseResponseSchema):
    correct_answers: int