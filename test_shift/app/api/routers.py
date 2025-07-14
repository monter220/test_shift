from fastapi import APIRouter

from test_shift.app.api.endpoints import user_router


main_router = APIRouter()
main_router.include_router(user_router)
