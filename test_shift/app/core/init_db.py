import contextlib
import datetime

from fastapi_users.exceptions import UserAlreadyExists
from pydantic import EmailStr

from test_shift.app.core.config import settings
from test_shift.app.core.db import get_async_session
from test_shift.app.core.user import get_user_db, get_user_manager
from test_shift.app.schemas import UserCreate


get_async_session_context = contextlib.asynccontextmanager(get_async_session)
get_user_db_context = contextlib.asynccontextmanager(get_user_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)


async def create_user(
        email: EmailStr,
        password: str,
        date_of_employment: datetime.date,
        celery: int,
        is_superuser: bool = False,
):
    try:
        async with get_async_session_context() as session:
            async with get_user_db_context(session) as user_db:
                async with get_user_manager_context(user_db) as user_manager:
                    await user_manager.create(
                        UserCreate(
                            email=email,
                            password=password,
                            date_of_employment=date_of_employment,
                            celery=celery,
                            is_superuser=is_superuser
                        )
                    )
    except UserAlreadyExists:
        pass


async def create_first_superuser():
    if (settings.first_superuser_email is not None
            and settings.first_superuser_password is not None):
        await create_user(
            email=settings.first_superuser_email,
            password=settings.first_superuser_password,
            date_of_employment=settings.first_superuser_date_of_employment,
            celery=1000000,
            is_superuser=True,
        )
