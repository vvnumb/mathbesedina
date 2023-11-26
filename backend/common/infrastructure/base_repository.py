from abc import ABC
from typing import Generic, Optional, List, Type, TypeVar

from sqlalchemy.orm import Session

from src.models.base import Base


T = TypeVar("T", bound=Base)

class BaseMixin(Generic[T]):
    _model: Type[T]
    _session: Session

    def __init__(
            self,
            session: Session
    ):
        self._session = session
        self.model_query = self._session.query(self._model)



class InsertMixin(BaseMixin[T]):
    """Добавляет метод добавления объекта в бд"""
    def insert(
            self,
            instance: T,
    ) -> None:
        self._session.add(instance=instance)


class RetrieveMixin(BaseMixin[T]):
    """Добавляет метод получение одного объекта (или None) из бд"""
    def get_single(
            self,
            *filters,
    ) -> Optional[T]:
        model = self.model_query.filter(*filters).first()
        self._session.expunge_all()
        return model


class ListMixin(BaseMixin[T]):
    """Добавляет метод для получения списка объектов"""
    def get_list(
            self,
            *filters,
    ) -> List[T]:
        # todo: Можно добавить пагинацию внутри self.model_query, либо добавить именованные параметры
        models = self.model_query.filter(*filters).all()
        self._session.expunge_all()
        return models


class UpdateMixin(BaseMixin[T]):
    """Добавляет метод обновления объекта из бд"""
    def update(
            self,
            instance: T,
    ) -> T:
        self.model_query.update(instance)
        return instance


class DeleteMixin(BaseMixin[T]):
    """Добавляет метод удаления объекта из бд"""
    def delete(
            self,
            instance: T,
    ) -> None:
        self._session.delete(instance)


class ReadMixin(RetrieveMixin[T], ListMixin[T]):
    """Позволяет читать данные из бд"""


class CRUMixin(InsertMixin[T], ReadMixin[T], UpdateMixin[T]):
    """Позволяет читать, добавлять и обновлять данные"""


class CRUDRepository(CRUMixin[T], DeleteMixin[T], ABC):
    """Повзоляет читать, добавлять, обновлять и удалять данные"""
