import pytest

from aoc2019.intcode import IntCode


def test_part1():
    intcode = IntCode()
    intcode.get_input("input/day_05")
    intcode.set_user_input([1])
    intcode.diagnostic_program()
    assert intcode.result == 16489636


@pytest.mark.parametrize(
    ("input_file", "user_input", "expected_result"),
    [
        ("input/day_05", [5], 9386583),
        ("input/day_05_ex_1", [0], 0)
    ]
)
def test_part2(input_file, user_input, expected_result):
    intcode = IntCode()
    intcode.get_input(input_file)
    intcode.set_user_input(user_input)
    intcode.diagnostic_program()
    assert intcode.result == expected_result
