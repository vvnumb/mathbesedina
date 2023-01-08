from enum import Enum


class TaskType(Enum):
    """Типы задания"""
    SINGLE = "SINGLE"
    FULL = "FULL"
    MANY = "MANY"


