from dataclasses import dataclass
from typing import List

from common.service_interface import SyncService
from src.infrastructure.unit_of_work.test import TestUnitOfWork
from src.models import Test


@dataclass(slots=True, frozen=True, kw_only=True)
class GetTestsListCase(SyncService):
	uow: TestUnitOfWork
	
	def __call__(self) -> List[Test]:
		with self.uow:
			return self.uow.tests.get_list()
