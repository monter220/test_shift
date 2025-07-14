from sqlalchemy import Column, Date, Integer

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable

from test_shift.app.core.db import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    celery = Column(Integer, nullable=False, default=10000)
    date_of_employment = Column(Date, nullable=False)
