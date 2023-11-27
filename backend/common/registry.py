from config import database_config
from src.api.v1.use_cases.test import GetTestsListCase
from src.api.v1.use_cases.test.get_single_test import GetSingleTestCase
from src.api.v1.use_cases.textbook import GetTextbooksCase, GetTopicsCase
from src.infrastructure.unit_of_work.test import TestUnitOfWork
from src.infrastructure.unit_of_work.textbook import TopicUnitOfWork
from src.api.v1.use_cases.textbook.get_single_topic import GetSingleTopicCase


class Registry:
	"""DI-контейнер"""
	
	@staticmethod
	def topic_unit_of_work() -> TopicUnitOfWork:
		return TopicUnitOfWork(session_maker=database_config.session_maker)
		
	@staticmethod
	def test_unit_of_work() -> TestUnitOfWork:
		return TestUnitOfWork(session_maker=database_config.session_maker)
	
	@staticmethod
	def get_textbooks_case() -> GetTextbooksCase:
		return GetTextbooksCase(uow=Registry.topic_unit_of_work())
	
	@staticmethod
	def get_topics_case() -> GetTopicsCase:
		return GetTopicsCase(uow=Registry.topic_unit_of_work())
	
	@staticmethod
	def get_single_topic_case() -> GetSingleTopicCase:
		return GetSingleTopicCase(uow=Registry.topic_unit_of_work())
	
	@staticmethod
	def get_tests_list_case() -> GetTestsListCase:
		return GetTestsListCase(uow=Registry.test_unit_of_work())
	@staticmethod
	def get_single_test_case() -> GetSingleTestCase:
		return GetSingleTestCase(uow=Registry.test_unit_of_work())
	