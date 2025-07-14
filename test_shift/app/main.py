import uvicorn
from fastapi import FastAPI

from test_shift.app.core.config import settings
from test_shift.app.api.routers import main_router
from test_shift.app.core.init_db import create_first_superuser


app = FastAPI(
    docs_url='/docs',
    redoc_url=None,
    title=settings.app_title,
)

app.include_router(main_router)


@app.on_event('startup')
async def startup():
    await create_first_superuser()


def start():
    uvicorn.run("test_shift.app.main:app", host="0.0.0.0", port=8000, reload=True,)


if __name__ == '__main__':
    start()
