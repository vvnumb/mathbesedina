from sqlalchemy import Column, Integer
from sqlalchemy.orm import declarative_mixin, declared_attr


@declarative_mixin
class IdMixin:
    """добавляет в модель стандартное поле id"""

    @declared_attr
    def __table_args__(cls):
        return {
            "extend_existing": True,
        }

    @declared_attr
    def id(cls):
        return Column(Integer, primary_key=True, autoincrement=True)
