from typing import Type, Optional, List

from fastapi import Depends
from sqlalchemy.orm import Session

from common.dependencies.current_session import CurrentSession
from common.orm.models.base import Base


class BaseMixin:
    model: Type[Base]


class InsertMixin(BaseMixin):
    """Добавляет метод добавления объекта в бд"""
    def insert(
            self,
            instance: "InsertMixin.model",
            session: Session = Depends(CurrentSession())
    ) -> None:
        session.add(instance=instance)


class RetrieveMixin(BaseMixin):
    """Добавляет метод получение одного объекта (или None) из бд"""
    def retrieve(
            self,
            session: Session = Depends(CurrentSession()),
            *filters,
            **named_filters
    ) -> Optional["RetrieveMixin.model"]:
        # todo: check this out!!!
        return session.query(self.model).filter(*filters).filter_by(**named_filters).first()


class ListMixin(BaseMixin):
    """Добавляет метод для получения списка объектов"""
    def list(
            self,
            session: Session = Depends(CurrentSession()),
            *filters,
            **named_filters
    ) -> List["ListMixin.model"]:
        # todo: check this out!!!
        return session.query(self.model).filter(*filters).filter_by(**named_filters).all()


class UpdateMixin(BaseMixin):
    """Добавляет метод обновления объекта из бд"""
    def update(
            self,
            instance: "UpdateMixin.model",
            data: dict,
            session: Session = Depends(CurrentSession())
    ) -> "UpdateMixin.model":
        for field, value in data.items():
            setattr(instance, field, value)
        session.query(self.model).update(instance)
        return instance


class DeleteMixin(BaseMixin):
    """Добавляет метод удаления объекта из бд"""
    def delete(
            self,
            instance: "DeleteMixin.model",
            session: Session = Depends(CurrentSession())
    ) -> None:
        session.delete(instance)


class ReadMixin(RetrieveMixin, ListMixin):
    """Позволяет читать данные из бд"""


class CRUMixin(InsertMixin, ReadMixin, UpdateMixin):
    """Позволяет читать, добавлять и обновлять данные"""


class CRUDMixin(CRUMixin, DeleteMixin):
    """Повзоляет читать, добавлять, обновлять и удалять данные"""
