from dataclasses import dataclass

from fastapi.security import OAuth2PasswordRequestForm

from common.exception import UserException
from common.service_interface import SyncService
from src.api.v1.use_cases.auth.password_service import PasswordService
from src.infrastructure.unit_of_work.user import UserUnitOfWork
from src.models import User


@dataclass(slots=True, frozen=True, kw_only=True)
class AuthenticateCase(SyncService):
	"""Получеение полной темы"""
	uow: UserUnitOfWork
	password_service: PasswordService
	
	def __call__(self, form_data: OAuth2PasswordRequestForm) -> User:
		with self.uow:
			user: User = self.uow.users.get_single(
				User.username == form_data.username,
				User.is_active == True
			)
		
		if not user:
			raise UserException
		
		if not self.password_service.verify_password(form_data.password, user.hashed_password):
			raise UserException
		
		return user
