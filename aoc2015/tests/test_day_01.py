import pytest

from aoc2015 import day_01

@pytest.mark.parametrize(
    ("input_string", "expected_result"),
    [
        ("(())", 0),
        ("()()", 0),
        ("(((", 3),
        ("(()(()(", 3),
        ("))(((((", 3),
        ("())", -1),
        ("))(", -1),
        (")))", -3),
        (")())())", -3),
    ]
)
def test_part1(input_string, expected_result):
    return_value = day_01._traverse_floors(0, input_string)
    assert return_value == expected_result


@pytest.mark.parametrize(
    ("input_string", "expected_result"),
    [
        (")", 1),
        ("()())", 5),
    ]
)
def test_part2(input_string, expected_result):
    return_value = day_01._find_first_basement_position(0, input_string)
    assert return_value == expected_result
