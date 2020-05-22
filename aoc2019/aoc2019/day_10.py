import collections
from decimal import Decimal
import math

from aoc2019 import point


def part1(input_file="input/day_10"):
    # Result: (28, 29)
    best_point = {
        "coordinates": point.Point(0, 0),
        "visible_points": 0
    }
    points = point.get_points_from_file(input_file)
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
    print(best_point['coordinates'], best_point['visible_points'])
    return best_point['coordinates'], best_point['visible_points']


def part2(input_file="input/day_10_p1_ex5"):
    # initial_point = point.Point(28, 29)
    initial_point = point.Point(11, 13)
    points = point.get_points_from_file(input_file)
    points.remove(initial_point)
    angles = {}
    for terminal_point in points:
        angle = _calculate_angle(terminal_point, initial_point)
        if angle not in angles:
            angles[angle] = [terminal_point]
        else:
            angles[angle].append(terminal_point)

    # todo: sort each angle list by distance
    for angle in angles:
        distances = []
        for terminal_point in angle:
            distances.append(_calculate_distance(terminal_point, initial_point))
    # todo: start at math.pi/2 and move clockwise, popping points from lists per angle

    for terminal_point in points:
        angle = _calculate_angle(terminal_point, initial_point)
        if angle < math.pi/2:
            angle -= math.pi
        while angle in angles:
            initial_point_tuple = (initial_point.x, initial_point.y)
            terminal_point_tuple = (terminal_point.x, terminal_point.y)
            existing_point_tuple = (angles[angle].x, angles[angle].y)
            if math.dist(initial_point_tuple, terminal_point_tuple) < math.dist(initial_point_tuple, existing_point_tuple):
                temp_point = angles[angle]
                angles[angle] = terminal_point
                terminal_point = temp_point
            angle += math.pi
        angles[angle] = terminal_point

    angle_keys = list(angles.keys())
    for i, angle in enumerate(sorted(angle_keys, reverse=True)):
        if i < 10:
            print(angle)
        if i == 199:
            print(angles[angle])
            print(angles[angle].x * 100 + angles[angle].y)
            break

def get_input(file_name, transform=None, delim='\n'):
    with open(file_name) as fh:
        lines = fh.read().split(delim)
        if transform:
            lines = [transform(line) for line in lines]
        return lines

def _get_distance(p1, p2):
        return Decimal(math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2))

def _calculate_angle(p1, p2):
    delta_y = p1.y - p2.y
    delta_x = p1.x - p2.x
    return math.atan2(delta_y, delta_x) * 180 / math.pi

def _calculate_distance(p1, p2):
    return decimal(math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2))

def _get_visible_angles(station, asteroids):
    angles = {}
    for asteroid in asteroids:
        if station is asteroid:
            continue
        angle = _calculate_angle(station, asteroid)
        if angles.get(angle):
            angles[angle].append(asteroid)
        else:
            angles[angle] = [asteroid]
    return angles
