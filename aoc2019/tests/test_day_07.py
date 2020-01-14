from unittest import mock
import pytest

from aoc2019 import day_07


@pytest.mark.parametrize(
    ("input_file", "permutations_result", "expected_result"),
    [
        ("input/day_07", [(2, 1, 4, 3, 0)], 298586),
        ("input/day_07_p1_ex1", [(4, 3, 2, 1, 0)], 43210),
        ("input/day_07_p1_ex2", [(0, 1, 2, 3, 4)], 54321),
        ("input/day_07_p1_ex3", [(1, 0, 4, 3, 2)], 65210),
    ]
)
@mock.patch("aoc2019.day_07.permutations")
def test_part1(mock_permutations, input_file, permutations_result, expected_result):
    mock_permutations.return_value = permutations_result
    result = day_07.part1(input_file=input_file)
    assert result == expected_result


@pytest.mark.parametrize(
    ("input_file", "permutations_result", "expected_result"),
    [
        ("input/day_07", [(8, 6, 7, 9, 5)], 9246095),
        ("input/day_07_p2_ex1", [(9, 8, 7, 6, 5)], 139629729),
        ("input/day_07_p2_ex2", [(9, 7, 8, 5, 6)], 18216)
    ]
)
@mock.patch("aoc2019.day_07.permutations")
def test_part2(mock_permutations, input_file, permutations_result, expected_result):
    mock_permutations.return_value = permutations_result
    result = day_07.part2(input_file=input_file)
    assert result == expected_result
