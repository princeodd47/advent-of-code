from common.read_file import get_input_as_strings
from common.point import Point


def part1():
    print(_get_tree_count('input/day_03'))


def _get_tree_count(input_file):
    position = Point(x=0, y=0)
    x_increment = 3
    y_increment = 1
    tree_count = 0
    grid = _create_grid_with_values(input_file)
    while position.y < len(grid):
        if _get_value_at_point(grid, position.x, position.y) == '#':
            tree_count += 1
        position.x += x_increment
        position.y += y_increment
    return tree_count


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
