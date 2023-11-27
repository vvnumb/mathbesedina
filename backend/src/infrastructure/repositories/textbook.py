from sqlalchemy.orm import joinedload

from common.infrastructure.base_repository import CRUDRepository
from src.models import Textbook, Topic, Video, VideoXTopic


class TextbookRepository(CRUDRepository[Textbook]):
    _model = Textbook


class TopicRepository(CRUDRepository[Topic]):
    _model = Topic
    
    def fetch_videos(self):
        self._model_query = self._model_query.options(joinedload(Topic.videos))
        return self
    
    def fetch_tests(self):
        self._model_query = self._model_query.options(joinedload(Topic.tests))
        return self


class VideoRepository(CRUDRepository[Video]):
    _model = Video
