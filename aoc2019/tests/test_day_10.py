import pytest

from aoc2019 import day_10
from aoc2019 import point


@pytest.mark.parametrize(
    ("input_file", "expected_point", "expected_visible_points"),
    [
        ("input/day_10_p1_ex1", point.Point(3, 4), 8),
        ("input/day_10_p1_ex2", point.Point(5, 8), 33),
        ("input/day_10_p1_ex3", point.Point(1, 2), 35),
        ("input/day_10_p1_ex4", point.Point(6, 3), 41),
        ("input/day_10_p1_ex5", point.Point(11, 13), 210),
        ("input/day_10", point.Point(28, 29), 340)
    ]
)
def test_part1(input_file, expected_point, expected_visible_points):
    best_point, visible_points = day_10.part1(input_file)
    assert best_point == expected_point
    assert visible_points == expected_visible_points

def test_part2():
    pass
