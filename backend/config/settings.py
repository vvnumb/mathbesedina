from typing import Optional, Any

from pydantic import BaseSettings, Field
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class BaseEnvSettings(BaseSettings):
    """Базовый класс для чтения переменных из окружения"""
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class UvicornSettings(BaseEnvSettings):
    """Параметры запуска приложения"""
    app: str = Field("config.asgi:application")

    port: int = Field(8000, env="PORT")
    reload: bool = Field(True, env="RELOAD")
    host: str = Field("127.0.0.1", env="HOST")
    use_colors: bool = Field(True, env="USE_COLORS")


class ApplicationSettings(BaseEnvSettings):
    """Параметры приложения"""
    title: str = Field("mathbesedina.ru")
    debug: bool = Field(False, env="DEBUG")
    docs_url = Field("/api/v1/docs")


class CORSSettings(BaseEnvSettings):
    """Параметры КОРС-ов"""
    allow_credentials: bool = Field(True)
    allow_methods: list[str] = Field(["*"])
    allow_headers: list[str] = Field(["*", "Authorization"])
    allow_origins: list[str] = Field(["*"], env="CORS_ORIGINS")


class DatabaseSettings(BaseEnvSettings):
    """Параметры подключения к БД"""
    user = Field("postgres", env="POSTGRES_USER")
    password = Field("postgres", env="POSTGRES_PASSWORD")
    host = Field("localhost", env="POSTGRES_HOST")
    port = Field("5432", env="POSTGRES_PORT")
    database = Field("mathbesedina", env="POSTGRES_DB")
    pool_size = Field(10, env="POSTGRES_POOL_SIZE")

    @property
    def url(self):
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"

    @property
    def engine(self):
        return create_engine(
            self.url,
            pool_pre_ping=True,
            pool_size=self.pool_size,
            max_overflow=0
        )

    @property
    def session_maker_class(self):
        return sessionmaker(autocommit=False, autoflush=False, bind=self.engine)


class AlembicSettings(BaseSettings):
    """Параметры таблиц БД в алембике"""
    target_metadata: Any
    connection: Optional[DatabaseSettings]

    @classmethod
    def generate(cls):
        from src.models.base import Base

        return cls(
            target_metadata=Base.metadata,
            connection=DatabaseSettings()
        )
