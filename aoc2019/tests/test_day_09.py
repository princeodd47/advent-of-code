import pytest

from aoc2019.intcode import IntCode


@pytest.mark.parametrize(
    ("input_file", "user_input", "expected_result"),
    [
        ("input/day_09_p1_ex2", [0], 1219070632396864),
        ("input/day_09_p1_ex3", [0], 1125899906842624)
    ]
)
def test_part1(input_file, user_input, expected_result):
    intcode = IntCode()
    intcode.get_input(input_file)
    intcode.set_user_input(user_input)
    intcode.diagnostic_program()
    assert intcode.result == expected_result


def test_part2():
    pass
