from common.infrastructure.base_unit_of_work import PostgresUnitOfWork
from src.infrastructure.repositories.test import AnswerRepository, TaskRepository, TestRepository


class TestUnitOfWork(PostgresUnitOfWork):
	tests: TestRepository
	tasks: TaskRepository
	answers: AnswerRepository
	
	def __enter__(self):
		self._session = self._session_maker()
		self.tests = TestRepository(self._session)
		self.tasks = TaskRepository(self._session)
		self.answers = AnswerRepository(self._session)
