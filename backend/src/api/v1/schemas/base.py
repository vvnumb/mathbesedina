from pydantic import BaseModel, RootModel


class BaseResponseSchema(BaseModel):
    """Любой ответ АПИ"""
    class Config:
        from_attributes = True


class BaseResponseRootSchema(RootModel):
    """Любой ответ АПИ"""
    class Config:
        from_attributes = True
