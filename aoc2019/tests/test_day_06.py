from aoc2019 import day_06


def test_part1():
    orbital_map = day_06.OrbitalMap("input/day_06")
    assert orbital_map.get_total_orbits() == 251208
