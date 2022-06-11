import pytest

from aoc2015 import day_03


@pytest.mark.parametrize(
    ("input_string", "expected_result"),
    [
        (">", 2),
        ("^>v<", 4),
        ("^v^v^v^v^v", 2),
    ]
)
def test_part2(input_string, expected_result):
    return_value = day_03.part1(input_string)
    assert return_value == expected_result
