from crud.tests import read_test_success_percent


def check_test_success(test_id: int, right_answers_percent: int):
    test_success_percent = read_test_success_percent(test_id)

    return right_answers_percent >= test_success_percent
