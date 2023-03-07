backend_models = [
    # todo: здесь список всех моделей из бэкенда
]


class DatabaseRouter:

    def db_for_read(self, model, **hints):
        return "default"

    def db_for_write(self, model, **hints):
        return "default"
