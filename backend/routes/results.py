from fastapi import APIRouter

from crud.results import create_results
from schemas.result import ResultCreate, ResultResponse

router = APIRouter()


@router.post('/add', response_model=ResultResponse)
async def add_results(results: ResultCreate):
    create_results(results)
    return ResultResponse(isSuccess=True, percent=100)
