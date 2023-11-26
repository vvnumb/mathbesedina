from dataclasses import dataclass
from typing import List, Optional

from common.service_interface import SyncService
from src.infrastructure.unit_of_work.textbook import TopicUnitOfWork
from src.models import Textbook


@dataclass(slots=True, frozen=True, kw_only=True)
class GetTextbooksCase(SyncService):
    """Получение учебников"""
    uow: TopicUnitOfWork

    def __call__(self, school_class: Optional[int] = None) -> List[Textbook]:
        filters = []
        if school_class is not None:
            filters.append(Textbook.school_class == school_class)
        
        with self.uow:
            response_list = self.uow.textbooks.get_list(*filters)
        
        return response_list
        