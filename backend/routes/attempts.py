from fastapi import APIRouter

from crud import create_results
from crud.answers import get_right_answers_by_test_id
from crud.attempts import create_attempt
from schemas.attempt import AttemptCreateRequest, AttemptCreate
from schemas.result import ResultResponse, ResultCreate
from utils.check_test_success import check_test_success
from utils.get_right_answers_percent import get_right_answers_percent

router = APIRouter()


@router.post('/add', response_model=ResultResponse)
async def add_attempt(attempt: AttemptCreateRequest):
    user_answers_ids = [answer.user_answer_id for answer in attempt.user_answers]
    right_answers_percent = get_right_answers_percent(user_answers_ids)
    right_answers = get_right_answers_by_test_id(attempt.test_id)

    attempt_id = create_attempt(
        AttemptCreate(
            username=attempt.username,
            test_id=attempt.test_id,
            right_answers_percent=right_answers_percent
        )
    )

    create_results([ResultCreate(attempt_id=attempt_id, **answer.model_dump()) for answer in attempt.user_answers])
    is_test_success = check_test_success(attempt.test_id, right_answers_percent)

    return ResultResponse(is_success=is_test_success, percent=right_answers_percent, right_answers=right_answers)
