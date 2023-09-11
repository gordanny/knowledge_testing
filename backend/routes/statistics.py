from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from crud.statistic import read_test_answers_stats, read_test_participants_qty
from schemas.statistic import StatisticsResponse
from schemas.user import UserInDBBase
from utils.current_user import get_current_user

router = APIRouter()


@router.get('/{test_id}', response_model=StatisticsResponse)
async def get_test_stats(test_id: int, current_user: Annotated[UserInDBBase, Depends(get_current_user)]):
    participants_qty = read_test_participants_qty(test_id)

    if not participants_qty:
        raise HTTPException(status_code=405, detail='Not found')

    return StatisticsResponse(
        participants_qty=participants_qty,
        answers_stats=read_test_answers_stats(test_id)
    )
