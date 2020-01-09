import pytest

from aoc2019 import day_03


@pytest.mark.parametrize(
    ("input_file", "expected_result"),
    [
        ("input/day_03_ex_1", 159),
        ("input/day_03_ex_2", 135),
    ]
)
        # ("input/day_03", 43848)
def test_part1(input_file, expected_result):
    result = day_03.get_manhattan_distance(input_file)
    assert result == expected_result


@pytest.mark.parametrize(
    ("input_file", "expected_result"),
    [
        ("input/day_03_small", 30),
        ("input/day_03_ex_1", 610),
        ("input/day_03_ex_2", 410),
    ]
)
# Problem answer is below, but takes too long.
# ("input/day_03", 43848)
def test_part2(input_file, expected_result):
    result = day_03.get_shortest_total_distance(input_file)
    assert result == expected_result
