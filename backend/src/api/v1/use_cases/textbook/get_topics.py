from dataclasses import dataclass
from typing import List

from common.service_interface import SyncService
from src.infrastructure.unit_of_work.textbook import TopicUnitOfWork
from src.models import Topic



@dataclass(slots=True, frozen=True, kw_only=True)
class GetTopicsCase(SyncService):
    
    uow: TopicUnitOfWork
    """Получение тем уроков для учебника"""

    def __call__(self, textbook_id: int) -> List[Topic]:
        with self.uow:
            return self.uow.topics.get_list(Topic.textbook_id == textbook_id)
