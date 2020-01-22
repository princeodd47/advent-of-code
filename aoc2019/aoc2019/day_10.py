import math

from aoc2019 import point


def part1():
    best_point = {
        "coordinates": point.Point(0, 0),
        "visible_points": 0
    }
    # points = point.get_points_from_file("input/day_10_p1_ex1", "#")
    points = point.get_points_from_file("input/day_10", "#")
    for initial_point in points:
        terminal_angles = set()
        for terminal_point in points:
            if terminal_point != initial_point:
                delta_y = terminal_point.y - initial_point.y
                delta_x = terminal_point.x - initial_point.x
                angle = math.atan2(delta_y, delta_x)
                terminal_angles.add(angle)
        visible_points = len(terminal_angles)
        if visible_points > best_point['visible_points']:
            best_point['coordinates'] = initial_point
            best_point['visible_points'] = visible_points
    print(best_point)


def part2():
    pass
