from common.orm.repository.base import BaseRepository
from common.orm.repository.mixins import CRUDMixin
from src.models import User


class UserRepository(BaseRepository, CRUDMixin):
    model = User
