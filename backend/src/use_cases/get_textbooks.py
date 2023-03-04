from typing import Optional, Type

from common.service_interface import SyncService
from src.repositories.textbook import TextbookRepository


class GetTextbooksCase(SyncService):
    """Получение учебников"""
    def __init__(
        self,
        textbook_repo: Type[TextbookRepository]
    ):
        self.textbook_repo = textbook_repo()

    def __call__(self, school_class: Optional[int] = None):
        filters = dict()
        if school_class is not None:
            filters.update(school_class=school_class)

        return self.textbook_repo.list(**filters)
