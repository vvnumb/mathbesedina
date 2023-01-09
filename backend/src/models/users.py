from sqlalchemy import Column, Integer, Boolean, String, DateTime

from src.models.base import Base


class User(Base):
    """
    Пользователь
    """

    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(
        String, index=True,
        comment='name of user',
    )
    middle_name = Column(
        String,
        comment='middle name of user',
    )
    last_name = Column(
        String, index=True,
        comment='last name of user',
    )

    email = Column(
        String,
        unique=True,
        index=True,
        nullable=False,
        comment='email',
    )
    username = Column(
        String,
        unique=True,
        nullable=True,
        comment='username',
    )
    hashed_password = Column(
        String,
        nullable=False,
        comment='passwd',
    )

    is_active = Column(
        Boolean,
        default=True,
        comment='locked or unlocked',
    )
    is_superuser = Column(
        Boolean,
        default=False,
    )
    is_subscribed = Column(
        Boolean,
        default=False,
    )

    created_at = Column(DateTime())
    updated_at = Column(DateTime())
    birth_date = Column(DateTime())
    subscription_ends = Column(DateTime())
    last_login_at = Column(DateTime())
