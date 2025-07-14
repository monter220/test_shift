import datetime

from typing import Optional
from pydantic import BaseModel
from fastapi_users import schemas


class UserRead(BaseModel):
    celery: int
    salary_review_date: datetime.date


class UserCreate(schemas.BaseUserCreate):
    celery: int
    date_of_employment: datetime.date


class UserUpdate(schemas.BaseUserUpdate):
    celery: Optional[int]
