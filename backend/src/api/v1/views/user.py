from fastapi import APIRouter, Depends
from fastapi.security import HTTPBasicCredentials
from sqlalchemy.orm import Session

from common.dependencies.security import oauth2_scheme
from common.dependencies.user import UserDependency
from src.models import User

# from common.dependencies.security import security

# from common.dependencies.current_session import CurrentSession

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
def get_single(
    user: User = Depends(UserDependency())
):
    """Ендпоинт-заглушка. Проверяет коннект к бд. Если все ок - возвращает null"""
    k = 1
    return {"ok": f"hello, {user.username}"}
    # from src.infrastructure.repositories.user import UserRepository
    # user_repo = UserRepository()
    # from src.models import User
    # u = user_repo.get_single(User.id == 2)
    # session.execute("Select 1")
