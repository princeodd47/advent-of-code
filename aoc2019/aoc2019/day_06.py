from aoc2019 import common


class OrbitalMap():
    def __init__(self, input_file):
        orbits = common.get_input_as_strings(input_file)
        self._map = self.generate_map(orbits)
        self._memo = {}
        self._memo_list = []

    def generate_map(self, data):
        orbital_map = {}
        for orbit in data:
            primary, satellite = orbit.split(')')
            orbital_map[satellite] = primary
        return orbital_map

    def _get_distance_to_obj(self, satellite, obj):
        if satellite == obj:
            return 0
        primary = self._map[satellite]
        if satellite not in self._memo:
            self._memo[satellite] = self._get_distance_to_obj(primary, obj) + 1
        distance = self._memo[satellite]
        self._memo.clear()
        return distance

    def get_total_orbits(self, obj):
        total = 0
        for satellite in self._map:
            total = total + self._get_distance_to_obj(satellite, obj)
        return total

    def _get_orbits_to_com(self, satellite):
        if satellite == "COM":
            return "COM"
        primary = self._map[satellite]
        if satellite not in self._memo_list:
            self._memo_list.append(satellite)
            self._get_orbits_to_com(primary)

    def get_distance_between_objects(self, obj1, obj2):
        obj1_orbits = []
        obj2_orbits = []
        if obj1 != "COM":
            obj1_primary = self._map[obj1]
        else:
            obj1_primary = obj1
        if obj2 != "COM":
            obj2_primary = self._map[obj2]
        else:
            obj2_primary = obj2

        while obj1_primary not in obj2_orbits and obj2_primary not in obj1_orbits:
            if obj1_primary != "COM":
                obj1_orbits.append(obj1_primary)
                obj1_primary = self._map[obj1_primary]
            if obj2_primary != "COM":
                obj2_orbits.append(obj2_primary)
                obj2_primary = self._map[obj2_primary]
        if obj1_primary in obj2_orbits:
            intersect = obj1_primary
            distance = obj2_orbits.index(intersect) + len(obj1_orbits)
        else:
            intersect = obj2_primary
            distance = obj1_orbits.index(intersect) + len(obj2_orbits)
        return distance

    def get_distance_2(self, obj1, obj2):
        self._get_orbits_to_com(obj1)
        obj1_orbits = self._memo_list
        self._memo_list.clear()
        obj2_orbits = []
        while obj2 not in obj1_orbits:
            obj2 = self._map[obj2]
            obj2_orbits.append(obj2)
            print(f"{obj2}")
        print(obj1_orbits.index(obj2))
        print(obj2_orbits.index(obj2))

def part1():
    orbital_map = OrbitalMap("input/day_06")
    return orbital_map.get_total_orbits("COM")

def part2():
    # orbital_map = OrbitalMap("input/day_06_p2_ex_1")
    # orbital_map = OrbitalMap("input/day_06")
    # # Solution 1 - Find path to COM for YOU and SAN, then find common, then add distances
    # orbital_map.get_orbits_to_com("YOU")
    # you_orbits = orbital_map._memo_list
    # # print(f"{you_orbits=}")
    # print(len(you_orbits))
    # orbital_map._memo_list.clear()
    # orbital_map.get_orbits_to_com("SAN")
    # san_orbits = orbital_map._memo_list
    # # print(f"{san_orbits=}")
    # print(len(san_orbits))
    # orbital_map._memo_list.clear()

    # Solution 2 - Walk back from YOU and SAN until meet, adding distance at each iteration
    orbital_map = OrbitalMap("input/day_06")
    distance = orbital_map.get_distance_between_objects("YOU", "SAN")
    print(f"{distance=}")

    orbital_map.get_distance_2("YOU", "SAN")
