from common.service_interface import SyncService
from src.repositories import TopicRepository


class GetTopicsCase(SyncService):
    """Получение тем уроков для учебника"""
    def __init__(
        self,
        topic_repo: TopicRepository
    ):
        self.topic_repo = topic_repo

    def __call__(self, textbook_id: int):
        filters = dict(
            textbook_id=textbook_id,
        )
        return self.topic_repo.list(**filters)

