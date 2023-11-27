from enum import Enum


class TaskType(str, Enum):
    """Типы задания"""
    SINGLE = "SINGLE"
    FULL = "FULL"
    MANY = "MANY"


