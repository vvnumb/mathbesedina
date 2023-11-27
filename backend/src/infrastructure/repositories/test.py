from sqlalchemy.orm import joinedload

from common.infrastructure.base_repository import CRUDRepository
from src.models import Task, TaskAnswer, Test


class TestRepository(CRUDRepository[Test]):
    _model = Test


class TaskRepository(CRUDRepository[Task]):
    _model = Task
    
    def fetch_answers(self):
        self._model_query = self._model_query.options(joinedload(Task.answers))
        return self


class AnswerRepository(CRUDRepository[TaskAnswer]):
    _model = TaskAnswer
    

