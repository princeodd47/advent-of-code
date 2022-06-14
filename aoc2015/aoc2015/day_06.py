from . import common
from . import light_plane

import re


def part1():
    lines = common.get_input_as_strings("input/day_06")
    input = _sanitize_input(lines)
    plane = light_plane.Plane()
    plane.commit_actions(input)
    print(plane.total_points_on)
    # answer: 569999


def _sanitize_input(lines):
    sanitized_input = []
    for line in lines:
        action_pattern = re.compile("^[a-zA-Z ]*")
        action = action_pattern.findall(line)[0].strip()

        points_pattern = re.compile("[0-9]*,[0-9]*")
        points = points_pattern.findall(line)
        begin_x = int(points[0].split(',')[0])
        begin_y = int(points[0].split(',')[1])
        end_x = int(points[1].split(',')[0])
        end_y = int(points[1].split(',')[1])

        d = {
            'action': action,
            'begin_x': begin_x,
            'begin_y': begin_y,
            'end_x': end_x,
            'end_y': end_y
        }
        sanitized_input.append(d)
    return sanitized_input


def part2():
    lines = common.get_input_as_strings("input/day_06")
    input = _sanitize_input(lines)
    plane = light_plane.Plane()
    plane.commit_actions_part2(input)
    print(plane.total_brightness)
    # answer: 17836115
