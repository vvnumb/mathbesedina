from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# from common.dependencies.current_session import CurrentSession

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
def get_single(
    # session: Session = Depends(CurrentSession())
):
    """Ендпоинт-заглушка. Проверяет коннект к бд. Если все ок - возвращает null"""
    # from src.infrastructure.repositories.user import UserRepository
    # user_repo = UserRepository()
    # from src.models import User
    # u = user_repo.get_single(User.id == 2)
    # session.execute("Select 1")
