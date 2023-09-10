from typing import Annotated

from fastapi import APIRouter, Depends

from crud.tests import read_tests
from schemas.test import TestBase
from schemas.user import UserInDBBase
from utils.current_user import get_current_user

router = APIRouter()


@router.get('/', response_model=list[TestBase])
async def get_tests(current_user: Annotated[UserInDBBase, Depends(get_current_user)]):
    return read_tests()
