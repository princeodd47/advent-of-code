from day_05 import main
import pytest


@pytest.mark.parametrize(
    ("input_file", "expected_result"),
    [
        ("tests/data/day_02_ex_1", 3500),
        ("tests/data/day_02_input", 5866714),
        ("tests/data/day_02_input_part2", 19690720)
    ]
)
def test_d2(input_file, expected_result):
    intcode = main.IntCode()
    intcode.get_input(input_file)
    assert intcode.diagnostic_program(1) == expected_result

def test_d5():
    intcode = main.IntCode()
    intcode.get_input("tests/data/input_d5")
    intcode.diagnostic_program(1)
    assert intcode.result == 16489636

def test_d5_examples():
    intcode = main.IntCode()
    intcode.data = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
    intcode.diagnostic_program(0)
    assert intcode.result == 0
