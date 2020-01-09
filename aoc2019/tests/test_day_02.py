import pytest

from aoc2019.intcode import IntCode


@pytest.mark.parametrize(
    ("input_file", "user_input", "expected_result"),
    [
        ("input/day_02_ex_1", 1, 3500),
        ("input/day_02", 1, 5866714),
        ("input/day_02_p2", 0, 19690720)
    ]
)
def test_d2(input_file, user_input, expected_result):
    intcode = IntCode()
    intcode.get_input(input_file)
    assert intcode.diagnostic_program(user_input) == expected_result
