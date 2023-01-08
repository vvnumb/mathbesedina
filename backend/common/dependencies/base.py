from abc import ABC, abstractmethod


class BaseDependency(ABC):
    """Интерфейс зависимостей"""

    @abstractmethod
    def __call__(self, *args, **kwargs):
        raise NotImplementedError
