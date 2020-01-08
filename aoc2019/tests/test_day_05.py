from aoc2019 import day_05
import pytest


@pytest.mark.parametrize(
    ("input_file", "user_input", "expected_result"),
    [
        ("tests/data/day_02_ex_1", 1, 3500),
        ("tests/data/day_02_input", 1, 5866714),
        ("tests/data/day_02_input_part2", 0, 19690720)
    ]
)
def test_d2(input_file, user_input, expected_result):
    intcode = day_05.IntCode()
    intcode.get_input(input_file)
    assert intcode.diagnostic_program(user_input) == expected_result

def test_d5p1():
    intcode = day_05.IntCode()
    intcode.get_input("tests/data/input_d5")
    intcode.diagnostic_program(1)
    assert intcode.result == 16489636

def test_d5_examples():
    intcode = day_05.IntCode()
    intcode.data = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
    intcode.diagnostic_program(0)
    assert intcode.result == 0

def test_d5p2():
    intcode = day_05.IntCode()
    intcode.get_input("tests/data/input")
    intcode.diagnostic_program(5)
    assert intcode.result == 9386583
