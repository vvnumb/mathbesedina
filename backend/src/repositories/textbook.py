from common.orm.repository.base import BaseRepository
from common.orm.repository.mixins import CRUDMixin
from src.models import Textbook, Topic


class TextbookRepository(BaseRepository, CRUDMixin):
    model = Textbook


class TopicRepository(BaseRepository, CRUDMixin):
    model = Topic
