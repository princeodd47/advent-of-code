import pytest
from unittest import mock

from aoc2015 import day_03


@pytest.mark.parametrize(
    ("input_string", "expected_result"),
    [
        (">", 2),
        ("^>v<", 4),
        ("^v^v^v^v^v", 2),
    ]
)
@mock.patch('aoc2015.day_03.common.get_input_as_single_string')
def test_part1(mock_get_input_as_single_string, input_string, expected_result):
    mock_get_input_as_single_string.return_value = input_string
    return_value = day_03.get_number_of_houses_visited()
    assert return_value == expected_result


@pytest.mark.parametrize(
    ("input_string", "expected_result"),
    [
        ("^v", 3),
        ("^>v<", 3),
        ("^v^v^v^v^v", 11),
    ]
)
@mock.patch('aoc2015.day_03.common.get_input_as_single_string')
def test_part2(mock_get_input_as_single_string, input_string, expected_result):
    mock_get_input_as_single_string.return_value = input_string
    return_value = day_03.get_number_of_houses_visited_with_robo()
    assert return_value == expected_result
