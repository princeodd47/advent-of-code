from dataclasses import dataclass


@dataclass
class Coordinates:
    x: int
    y: int

    def move_left(self, distance=1):
        self.x -= distance

    def move_right(self, distance=1):
        self.x += distance

    def move_up(self, distance=1):
        self.y += distance

    def move_down(self, distance=1):
        self.y -= distance


def get_slope(initial_point, terminal_point):
    numerator = terminal_point.y - initial_point.y
    denominator = terminal_point.x - initial_point.x
    if denominator == 0:
        slope = -1
    else:
        slope = numerator / denominator
    return slope


def get_points_from_file(input_file, target_character='#'):
    points = []
    with open(input_file, 'r') as fh:
        for y, line in enumerate(fh.readlines(0)):
            for x, char in enumerate(line):
                if char == target_character:
                    points.append(Point(x, y))
    return points
