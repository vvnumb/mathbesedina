from abc import ABC, abstractmethod
from typing import Any


class SyncService(ABC):
    """Интерфейс синхронного сервиса"""

    @abstractmethod
    def __call__(self, *args, **kwargs) -> Any:
        raise NotImplementedError


class AsyncService(ABC):
    """Интерфейс асинхронного сервиса"""

    @abstractmethod
    async def __call__(self, *args, **kwargs) -> Any:
        raise NotImplementedError
