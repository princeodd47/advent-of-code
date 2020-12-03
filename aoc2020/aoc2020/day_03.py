import math

from common.read_file import get_input_as_strings
from common.point import Point


def part1():
    slopes = [(3, 1)]
    print(_get_tree_count('input/day_03', slopes))
    # answer: 173


def part2():
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    print(_get_tree_count('input/day_03', slopes))
    # answer: 4385176320
    # tree count per slope: [82, 173, 84, 80, 46]


def _get_tree_count(input_file, slopes):
    slope_tree_count = []
    grid = _create_grid_with_values(input_file)
    for slope in slopes:
        position = Point(x=0, y=0)
        tree_count = 0
        while position.y < len(grid):
            if _get_value_at_point(grid, position.x, position.y) == '#':
                tree_count += 1
            position.x += slope[0]
            position.y += slope[1]
        slope_tree_count.append(tree_count)
    print(slope_tree_count)
    return math.prod(slope_tree_count)


def _create_grid_with_values(input_file):
    grid = []
    lines = get_input_as_strings(input_file)
    for line in lines:
        grid.append(line)
    return grid


def _get_value_at_point(grid, x, y):
    length = len(grid[y])
    max_index = length - 1
    while max_index < x:
        x -= length
    return grid[y][x]
