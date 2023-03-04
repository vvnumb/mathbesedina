from pydantic import BaseModel


class BaseResponseSchema(BaseModel):
    """Любой ответ АПИ"""
    class Config:
        orm_mode = True
