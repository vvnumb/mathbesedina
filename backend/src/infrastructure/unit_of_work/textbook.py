from common.infrastructure.base_unit_of_work import PostgresUnitOfWork
from src.infrastructure.repositories.textbook import TextbookRepository, TopicRepository, \
	VideoRepository


class TopicUnitOfWork(PostgresUnitOfWork):
	textbooks: TextbookRepository
	topics: TopicRepository
	videos: VideoRepository
	
	def __enter__(self):
		self._session = self._session_maker()
		
		self.textbooks = TextbookRepository(self._session)
		self.topics = TopicRepository(self._session)
		self.videos = VideoRepository(self._session)
