from .common import get_input

def part1():
    total = 0
    nums = get_input("input/day_01")
    for num in nums:
        total = total + (num//3)-2
    return total


def part2():
    modules = get_input("input/day_01")
    total = sum(get_fuel(module) for module in modules)
    return total


def get_fuel(mass):
    new_fuel = (mass//3)-2
    if new_fuel <= 0:
        return 0
    return new_fuel + get_fuel(new_fuel)
