import pytest

from aoc2019 import day_06


@pytest.mark.parametrize(
    ("input_file", "expected_result"),
    [
        ("input/day_06_p1_ex_1", 42),
        ("input/day_06", 251208)
    ]
)
def test_part1(input_file, expected_result):
    orbital_map = day_06.OrbitalMap(input_file)
    assert orbital_map.get_total_orbits("COM") == expected_result


@pytest.mark.parametrize(
    ("input_file", "expected_result"),
    [
        ("input/day_06_p2_ex_1", 4),
        ("input/day_06", 397)
    ]
)
def test_part2(input_file, expected_result):
    orbital_map = day_06.OrbitalMap(input_file)
    assert orbital_map.get_distance_between_objects("YOU", "SAN") == expected_result
