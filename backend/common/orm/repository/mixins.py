from typing import Type, Optional, List, Any

from sqlalchemy.orm import Session, Query

from common.dependencies.current_session import get_session
from src.models.base import Base


class BaseMixin:
    model: Type[Base]
    session: Session

    def __init__(
            self,
            session: Any = next(get_session())
    ):
        self.session = session
        self.model_query = self.session.query(self.model)


class JoinMixin(BaseMixin):

    def join(
            self,
            join_model: Type[Base],
            *conditions
    ) -> Query:
        self.model_query = self.model_query.join(join_model, *conditions)
        return self.model_query


class InsertMixin(BaseMixin):
    """Добавляет метод добавления объекта в бд"""
    def insert(
            self,
            instance: "InsertMixin.model",
    ) -> None:
        self.session.add(instance=instance)


class RetrieveMixin(BaseMixin):
    """Добавляет метод получение одного объекта (или None) из бд"""
    def retrieve(
            self,
            *filters,
            **named_filters
    ) -> Optional["RetrieveMixin.model"]:
        return self.model_query.filter(*filters).filter_by(**named_filters).first()


class ListMixin(BaseMixin):
    """Добавляет метод для получения списка объектов"""
    def list(
            self,
            *filters,
            **named_filters
    ) -> List["ListMixin.model"]:
        # todo: Можно добавить пагинацию внутри self.model_query, либо добавить именованные параметры
        return self.model_query.filter(*filters).filter_by(**named_filters).all()


class UpdateMixin(BaseMixin):
    """Добавляет метод обновления объекта из бд"""
    def update(
            self,
            instance: "UpdateMixin.model",
            data: dict,
    ) -> "UpdateMixin.model":
        for field, value in data.items():
            setattr(instance, field, value)
        self.model_query.update(instance)
        return instance


class DeleteMixin(BaseMixin):
    """Добавляет метод удаления объекта из бд"""
    def delete(
            self,
            instance: "DeleteMixin.model",
    ) -> None:
        self.session.delete(instance)


class ReadMixin(RetrieveMixin, ListMixin, JoinMixin):
    """Позволяет читать данные из бд"""


class CRUMixin(InsertMixin, ReadMixin, UpdateMixin):
    """Позволяет читать, добавлять и обновлять данные"""


class CRUDMixin(CRUMixin, DeleteMixin):
    """Повзоляет читать, добавлять, обновлять и удалять данные"""
