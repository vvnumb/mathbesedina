from common.metaclasses import Singleton
from config import database_config
from src.infrastructure.unit_of_work.textbook import TopicUnitOfWork
from src.use_cases import GetTextbooksCase, GetTopicsCase
from src.use_cases.get_single_topic import GetSingleTopicCase


class Registry:
	"""DI-контейнер"""
	
	@staticmethod
	def topic_unit_of_work() -> TopicUnitOfWork:
		return TopicUnitOfWork(session_maker=database_config.session_maker)
	
	@staticmethod
	def get_textbooks_case() -> GetTextbooksCase:
		return GetTextbooksCase(uow=Registry.topic_unit_of_work())
	
	@staticmethod
	def get_topics_case() -> GetTopicsCase:
		return GetTopicsCase(uow=Registry.topic_unit_of_work())
	
	@staticmethod
	def get_single_topic_case() -> GetSingleTopicCase:
		return GetSingleTopicCase(uow=Registry.topic_unit_of_work())
	