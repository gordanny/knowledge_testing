from crud import get_right_answers


def get_right_answers_percent(answers: list[int]):
    right_answers_amount = len(get_right_answers(answers))
    # TODO replace by questions amount query
    answers_mount = len(answers)
    right_answers_percent = int(right_answers_amount / answers_mount * 100)

    return right_answers_percent
