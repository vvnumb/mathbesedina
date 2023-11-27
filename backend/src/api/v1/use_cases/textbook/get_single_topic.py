from dataclasses import dataclass

from common.service_interface import SyncService
from src.infrastructure.unit_of_work.textbook import TopicUnitOfWork
from src.models import Topic


@dataclass(slots=True, frozen=True, kw_only=True)
class GetSingleTopicCase(SyncService):
	"""Получеение полной темы"""
	uow: TopicUnitOfWork
	
	def __call__(self, topic_id: int) -> Topic:
		with self.uow:
			topic = self.uow.topics.fetch_videos().fetch_tests().get_single(Topic.id == topic_id)
		return topic
