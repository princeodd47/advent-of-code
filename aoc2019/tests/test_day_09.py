import pytest

from aoc2019.intcode import IntCode


@pytest.mark.parametrize(
    ("input_file", "user_input", "expected_result"),
    [
        ("input/day_09_p1_ex2", [0], 1219070632396864),
        ("input/day_09_p1_ex3", [0], 1125899906842624),
        ("input/day_09", [1], 3638931938)
    ]
)
def test_part1(input_file, user_input, expected_result):
    intcode = IntCode()
    intcode.get_input(input_file)
    intcode.set_user_input(user_input)
    intcode.diagnostic_program()
    assert intcode.result == expected_result


def test_quine():
    ex1 = IntCode()
    ex1.get_input("input/day_09_p1_ex1")
    ex1.diagnostic_program()
    assert ex1.result_history == [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]


def test_part2():
    pass
