import json

from jose import JWTError, jwt
from fastapi import Depends
from sqlalchemy.orm import Session

from common.dependencies.base import BaseDependency
from common.dependencies.security import oauth2_scheme
from common.exception import CredentialException
from common.registry import Registry
from config import JWTSettings, jwt_config
from src.infrastructure.unit_of_work.user import UserUnitOfWork
from src.models import User


class UsernameDependency(BaseDependency):
    """Получение пользователя из JWT"""
    def __init__(
        self,
        jwt_config_: JWTSettings = jwt_config
    ):
        self.jwt_config = jwt_config_

    def __call__(self, token: str = Depends(oauth2_scheme)) -> str:
        try:
            payload = jwt.decode(
                token,
                self.jwt_config.SECRET_KEY,
                algorithms=[self.jwt_config.ALGORITHM]
            )
        except JWTError:
            raise CredentialException
        
        username: str = payload.get("sub")
        
        if not username:
            raise CredentialException
        
        return username



class UserDependency(BaseDependency):
    def __init__(
            self,
            uow: UserUnitOfWork = Registry.user_unit_of_work()
    ):
        self.uow = uow
        
    def __call__(self, username: str = Depends(UsernameDependency())) -> User:
        with self.uow:
            user: User = self.uow.users.get_single(
                User.username == username,
                User.is_active == True
            )
        
        if not user:
            raise CredentialException
        
        return user