from common.orm.repository.base import BaseRepository
from common.orm.repository.mixins import CRUDMixin
from src.models import Textbook


class TextbookRepository(BaseRepository, CRUDMixin):
    model = Textbook
