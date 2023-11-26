from abc import ABC, abstractmethod

from sqlalchemy.orm import Session, sessionmaker


class AbstractUnitOfWork(ABC):
	@abstractmethod
	def __enter__(self):
		...

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.rollback()

	@abstractmethod
	def commit(self):
		...

	@abstractmethod
	def rollback(self):
		...
	

class PostgresUnitOfWork(AbstractUnitOfWork, ABC):
	_session: Session
	_session_maker: sessionmaker = sessionmaker
	def __init__(self, session_maker: sessionmaker = sessionmaker):
		self._session_maker = session_maker
		
	def commit(self):
		self._session.commit()
	
	def rollback(self):
		self._session.rollback()
		self._session.expunge_all()
		self._session.close()
	
	def __exit__(self, exc_type, exc_val, exc_tb):
		super().__exit__(exc_type, exc_val, exc_tb)
		self._session.close()
	