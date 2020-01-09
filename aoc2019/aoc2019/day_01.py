from .common import get_input

def part1():
    print(get_total_fuel("input/day_01"))


def part2():
    print(get_total_fuel_nested("input/day_01"))


def get_total_fuel(input_file):
    total = 0
    nums = get_input(input_file)
    for num in nums:
        total = total + (num//3)-2
    return total


def get_total_fuel_nested(input_file):
    modules = get_input(input_file)
    total = sum(get_fuel(module) for module in modules)
    return total


def get_fuel(mass):
    new_fuel = (mass//3)-2
    if new_fuel <= 0:
        return 0
    return new_fuel + get_fuel(new_fuel)
