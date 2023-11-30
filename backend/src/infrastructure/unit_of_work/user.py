from common.infrastructure.base_unit_of_work import PostgresUnitOfWork
from src.infrastructure import UserRepository


class UserUnitOfWork(PostgresUnitOfWork):
	users: UserRepository
	def __enter__(self):
		self._session = self._session_maker()
		
		self.users = UserRepository(self._session)
