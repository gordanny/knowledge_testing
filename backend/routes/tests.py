from fastapi import APIRouter

from crud.tests import read_tests
from schemas.test import TestBase

router = APIRouter()


@router.get('/', response_model=list[TestBase])
async def get_tests():
    return read_tests()
