from fastapi import APIRouter
from . import users
from . import login
from . import tests
from . import results
from . import attempts

api_router = APIRouter()

api_router.include_router(login.router, tags=['Login'])
api_router.include_router(users.router, prefix='/users', tags=['Users'])
api_router.include_router(tests.router, prefix='/tests', tags=['Tests'])
api_router.include_router(attempts.router, prefix='/attempts', tags=['Attempts'])
