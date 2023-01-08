from common.dependencies.base import BaseDependency
from config import database_config


class CurrentSession(BaseDependency):
    """Получение соединения с базой данных"""

    def __init__(self):
        self.session = database_config.session_maker_class()

    def __call__(self):
        try:
            yield self.session
        finally:
            self.session.close()
