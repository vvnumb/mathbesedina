from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from common.dependencies.current_session import CurrentSession

router = APIRouter()


@router.get("/")
def get_single(
    session: Session = Depends(CurrentSession())
):
    from src.repositories.user import UserRepository
    user_repo = UserRepository()
    from src.models import User
    u = user_repo.retrieve(User.id == 2)
    session.execute("Select 1")
