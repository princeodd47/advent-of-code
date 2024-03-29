from dataclasses import dataclass


@dataclass
class Submarine:
    x: int
    y: int
    aim: int

    def increase_aim(self, amount):
        self.aim += amount

    def decrease_aim(self, amount):
        self.aim -= amount

    def move_forward(self, amount):
        self.x += amount
        self.y += self.aim * amount


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
