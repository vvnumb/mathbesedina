from sqlalchemy import Boolean, Column, Integer, String, Text, ForeignKey, \
    Enum as ORMEnum
from sqlalchemy.orm import relationship

from common.orm.models.enums import TaskType
from common.orm.models.model_mixins import IdMixin
from src.models import Base


class Textbook(Base, IdMixin):
    """Учебник"""
    school_class = Column(Integer, default=5)
    title = Column(String)
    slug = Column(String, unique=True, )  # mb deprecated

    topics = relationship("Topic", back_populates="textbook", uselist=True, )


class VideoXTopic(Base):
    """Сопоставление темам - видео"""
    __table_args__ = {
        "extend_existing": True,
    }
    __tablename__ = "video_x_topic"
    video_id = Column(
        Integer,
        ForeignKey("video.id"),
        primary_key=True,
    )
    topic_id = Column(
        Integer,
        ForeignKey("topic.id"),
        primary_key=True,
    )


class TestXTopic(Base):
    """Сопоставление тестов для тем"""
    __table_args__ = {
        "extend_existing": True,
    }
    __tablename__ = "test_x_topic"
    test_id = Column(
        Integer,
        ForeignKey("test.id"),
        primary_key=True,
    )
    topic_id = Column(
        Integer,
        ForeignKey("topic.id"),
        primary_key=True,
    )


class Topic(IdMixin, Base):
    """Тема"""
    textbook_id = Column(
        Integer,
        ForeignKey("textbook.id"),
        nullable=False,
        index=True,
    )
    title = Column(String, comment="название темы")
    description = Column(Text, comment="описание занятия")
    slug = Column(String, unique=True, comment="строка для url")  # mb deprecated

    videos = relationship("Video", secondary=VideoXTopic.__tablename__, back_populates="topics")
    tests = relationship("Test", secondary=TestXTopic.__tablename__, back_populates="topics")
    textbook = relationship("Textbook", back_populates="topics")


class Video(IdMixin, Base):
    """Видео"""
    title = Column(String, comment="название видео")
    link = Column(String, comment="ссылка на видео в источнике")

    topics = relationship("Topic", secondary=VideoXTopic.__tablename__,
                          back_populates="videos")


class TaskAnswer(IdMixin, Base):
    """Ответ на задание"""
    __tablename__ = "task_answer"
    task_id = Column(
        Integer,
        ForeignKey("task.id"),
        nullable=True, index=True
    )
    title = Column(String, comment="текст варианта ответа")
    is_right = Column(Boolean, nullable=False, server_default='False', default=False)

    task = relationship("Task", backref="answers", foreign_keys=[task_id])

class Task(IdMixin, Base):
    """Задание"""
    task_type = Column(ORMEnum(TaskType))
    task_text = Column(Text)

    image_link = Column(String, comment="ссылка на картинку для задачи")
    test_id = Column(
        Integer,
        ForeignKey("test.id"),
        nullable=False, index=True
    )

    test = relationship("Test", back_populates="tasks", foreign_keys=[test_id])
    # note: есть поле answers - задается через TaskAnswer backref
    # answers = relationship("TaskAnswer", backref="task", uselist=True)


class Test(IdMixin, Base):
    """Тест с заданиями"""
    title = Column(String, comment="название")
    description = Column(String, comment="описание")
    slug = Column(String, unique=True, comment="строка для url")  # mb deprecated
    school_class = Column(Integer)

    topics = relationship("Topic", secondary=TestXTopic.__tablename__, back_populates="tests")
    tasks = relationship("Task", back_populates="test", uselist=True)
