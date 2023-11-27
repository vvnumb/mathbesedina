from dataclasses import dataclass

from common.service_interface import SyncService
from src.infrastructure.unit_of_work.test import TestUnitOfWork
from src.models import Task


@dataclass(slots=True, frozen=True, kw_only=True)
class GetSingleTestCase(SyncService):
	uow: TestUnitOfWork
	
	def __call__(self, test_id: int):
		with self.uow:
			tasks = self.uow.tasks.fetch_answers().get_list(Task.test_id == test_id)
		
		return tasks