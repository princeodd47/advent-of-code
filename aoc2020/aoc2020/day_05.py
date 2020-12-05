import math
import statistics

from common.read_file import get_input_as_strings


class PlaneSeat():
    def __init__(self, string, lower, upper, minimum, maximum):
        self.string = string
        self.lower = lower
        self.upper = upper
        self.min = minimum
        self.max = maximum
        self.num_range = [self.min, self.max]
        self.prev_dir = None

    def get_position(self):
        if not self.string:
            if self.prev_dir == 'lower':
                return self.num_range[0]
            return self.num_range[1] - 1
        if self.string[0] == self.lower:
            self.prev_dir = 'lower'
            self.num_range[1] = statistics.median(self.num_range)
        else:
            self.prev_dir = 'upper'
            self.num_range[0] = statistics.median(self.num_range)
        self.string = self.string[1:]
        return self.get_position()


def part1():
    print(_get_max_seat_id('input/day_05'))
    # answer: 904


def part2():
    print(_get_empty_seat_id('input/day_05'))
    # answer: 669


def _get_max_seat_id(input_file):
    coordinates = _get_seat_coordinates(input_file)
    seat_ids = []
    for c in coordinates:
        seat_ids.append(_calculate_seat_id(c))
    return max(seat_ids)


def _get_empty_seat_id(input_file):
    coordinates = _get_seat_coordinates(input_file)
    begin_row = coordinates[0][0]
    end_row = coordinates[-1][0]
    missing = _get_empty_seats(coordinates)
    valid_seat = _find_valid_seat(begin_row, end_row, missing)
    if valid_seat:
        return _calculate_seat_id(valid_seat)
    return 'too many missing seats'


def _get_seat_coordinates(input_file):
    lines = get_input_as_strings(input_file)
    coordinates = []
    for line in lines:
        row = line[:7]
        col = line[-3:]
        seat = PlaneSeat(string=row, lower='F', upper='B', minimum=0, maximum=128)
        row_num = math.trunc(seat.get_position())
        seat = PlaneSeat(string=col, lower='L', upper='R', minimum=0, maximum=8)
        col_num = math.trunc(seat.get_position())
        coordinates.append((row_num, col_num))
    coordinates.sort(key=lambda tup: (tup[0], tup[1]))
    return coordinates


def _calculate_seat_id(coordinate):
    return (coordinate[0] * 8) + coordinate[1]


def _get_empty_seats(coordinates):
    missing = []
    begin = coordinates[0]
    end = coordinates[-1]
    current = [begin[0], begin[1]]
    while current[0] <= end[0]:
        while current[1] <= 7:
            if (current[0], current[1]) not in coordinates:
                missing.append(tuple(current))
            current[1] += 1
        current[0] += 1
        current[1] = 0
    return missing


def _find_valid_seat(begin_row, end_row, missing):
    valid_seat = []
    for m in missing:
        if begin_row < m[0] < end_row:
            valid_seat.append(m)
    if len(valid_seat) == 1:
        return valid_seat[0]
    return None
