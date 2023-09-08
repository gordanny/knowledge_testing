from fastapi import APIRouter
from . import user
from . import login
from . import tests
from . import attempts

api_router = APIRouter()

api_router.include_router(login.router, tags=['Login'])
api_router.include_router(user.router, prefix='/user', tags=['User'])
api_router.include_router(tests.router, prefix='/tests', tags=['Tests'])
api_router.include_router(attempts.router, prefix='/attempts', tags=['Attempts'])
