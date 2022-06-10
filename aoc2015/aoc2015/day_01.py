from . import common


def part1():
    instructions = _get_instructions("input/day_01")
    starting_floor = 0
    destination_floor = _traverse_floors(starting_floor, instructions)
    print(destination_floor)


def _get_instructions(input_file):
    input_lines = common.get_input_as_strings(input_file)
    return input_lines[0]


def _traverse_floors(starting_floor, instructions):
    current_floor = starting_floor
    for i in instructions:
        if i == "(":
            current_floor += 1
        elif i == ")":
            current_floor -= 1
    return current_floor
