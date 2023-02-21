from typing import Type, Optional, List, Any

from sqlalchemy.orm import Session

from common.dependencies.current_session import CurrentSession
from src.models.base import Base


class BaseMixin:
    model: Type[Base]
    session: Session

    def __init__(
            self,
            session: Any = CurrentSession()()
    ):
        self.session = next(session)


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
        return self.session.query(self.model).filter(*filters).filter_by(**named_filters).first()


class ListMixin(BaseMixin):
    """Добавляет метод для получения списка объектов"""
    def list(
            self,
            *filters,
            **named_filters
    ) -> List["ListMixin.model"]:
        # todo: rework limit_offset pagination
        return self.session.query(self.model).filter(*filters).filter_by(**named_filters).all()


class UpdateMixin(BaseMixin):
    """Добавляет метод обновления объекта из бд"""
    def update(
            self,
            instance: "UpdateMixin.model",
            data: dict,
    ) -> "UpdateMixin.model":
        for field, value in data.items():
            setattr(instance, field, value)
        self.session.query(self.model).update(instance)
        return instance


class DeleteMixin(BaseMixin):
    """Добавляет метод удаления объекта из бд"""
    def delete(
            self,
            instance: "DeleteMixin.model",
    ) -> None:
        self.session.delete(instance)


class ReadMixin(RetrieveMixin, ListMixin):
    """Позволяет читать данные из бд"""


class CRUMixin(InsertMixin, ReadMixin, UpdateMixin):
    """Позволяет читать, добавлять и обновлять данные"""


class CRUDMixin(CRUMixin, DeleteMixin):
    """Повзоляет читать, добавлять, обновлять и удалять данные"""
