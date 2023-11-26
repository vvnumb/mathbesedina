from common.infrastructure.base_repository import CRUDRepository
from src.models import User


class UserRepository(CRUDRepository[User]):
    _model = User
