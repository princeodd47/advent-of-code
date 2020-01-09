from aoc2019 import common


class OrbitalMap():
    def __init__(self, input_file):
        orbits = common.get_input_as_strings(input_file)
        self._map = self.generate_map(orbits)
        self._memo = {}

    def generate_map(self, data):
        orbital_map = {}
        for orbit in data:
            primary, satellite = orbit.split(')')
            orbital_map[satellite] = primary
        return orbital_map


    def _get_distance_to_com(self, satellite):
        if satellite == "COM":
            return 0
        primary = self._map[satellite]
        if satellite not in self._memo:
            self._memo[satellite] = self._get_distance_to_com(primary) + 1
        return self._memo[satellite]

    def get_total_orbits(self):
        total = 0
        for satellite in self._map:
            total = total + self._get_distance_to_com(satellite)
        return total

def part1():
    orbital_map = OrbitalMap("input/day_06")
    return orbital_map.get_total_orbits()
