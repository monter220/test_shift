import datetime
from sqlalchemy.ext.asyncio import AsyncSession

from test_shift.app.schemas import UserRead
from test_shift.app.models import User


async def get_user_celery(
        user: User,
        session: AsyncSession,
) -> UserRead:
    salary_review_date = user.date_of_employment
    while salary_review_date < datetime.date.today():
        salary_review_date = salary_review_date +  datetime.timedelta(days=180)
    return UserRead(
        celery=user.celery,
        salary_review_date=salary_review_date
    )
