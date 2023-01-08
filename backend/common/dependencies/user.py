import json

from fastapi import Depends
from fastapi_jwt_auth import AuthJWT
from sqlalchemy.orm import Session

from common.dependencies.base import BaseDependency
from common.dependencies.current_session import CurrentSession


class OptionalCurrentUser(BaseDependency):
    """Получение пользователя из JWT"""
    def __init__(
        self,
        session: Session = Depends(CurrentSession()),
        authorizer: AuthJWT = Depends()
    ):
        self.session: Session = session
        self.authorizer: AuthJWT = authorizer

    def __call__(self):
        self.authorizer.jwt_required()
        payload = self._get_payload()
        user_id = self._fetch_id(payload)
        # todo: here is work with user_repo
        # user = self.user_repo.retrieve(id=user_id)
        user = None
        return user

    def _get_payload(self):
        payload = self.authorizer.get_jwt_subject()
        return json.loads(payload)

    def _fetch_id(self, payload: dict):
        user_id = payload.get("id", None)
        if user_id is None:
            raise KeyError("Token is incorrect")

        return user_id
