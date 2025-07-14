from fastapi import (
    APIRouter,
    Depends,
)
from sqlalchemy.ext.asyncio import AsyncSession

from test_shift.app.core.db import get_async_session
from test_shift.app.core.user import auth_backend, fastapi_users, current_user
from test_shift.app.schemas import UserRead
from test_shift.app.models import User
from test_shift.app.crud import get_user_celery


router = APIRouter()

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix='/auth/jwt',
    tags=['auth'],
)


@router.get(
    '/me',
    response_model=UserRead,
)
async def get_celery(
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user),
):
    return await get_user_celery(user = user, session=session)
