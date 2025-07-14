import datetime

from pydantic_settings import BaseSettings
from pydantic import EmailStr


class Settings(BaseSettings):
    app_title: str = 'ШИФТ'
    database_url: str = 'sqlite+aiosqlite:///./shift.db'
    secret: str = 'secret'
    first_superuser_email: EmailStr = 'testingemail@mail.ru'
    first_superuser_password: str = 'MegaTest123)(*'
    first_superuser_date_of_employment: datetime.date = '2025-01-01'

    class Config:
        env_file = '.env'


settings = Settings()
