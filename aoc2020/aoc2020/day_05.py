import statistics

from common.read_file import get_input_as_strings


class Plane():
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
            # print(f'{self.string[0]} lower')
            self.prev_dir = 'lower'
            # self.max -= (self.max - self.min)/2
            self.num_range[1] = statistics.median(self.num_range)
        else:
            # print(f'{self.string[0]} upper')
            self.prev_dir = 'upper'
            # self.min += (self.max - self.min)/2
            self.num_range[0] = statistics.median(self.num_range)
        # print(f'{self.min=} {self.max=}')
        self.string = self.string[1:]
        return self.get_position()


def part1():
    print(_get_seat_num('input/day_05'))


def part2():
    print(_get_seat_num('input/day_05'))


def _get_seat_num(input_file):
    lines = get_input_as_strings(input_file)
    seat_ids = []
    coordinates = []
    for line in lines:
        row = line[:7]
        col = line[-3:]
        # print(f'{line=} {row=} {col=}')
        plane = Plane(row, 'F', 'B', 0, 128)
        row_num = plane.get_position()
        # print(f'{row_num=}')
        plane = Plane(col, 'L', 'R', 0, 8)
        col_num = plane.get_position()
        # print(f'{col_num=}')
        seat_id = _calculate_seat_id(row_num, col_num)
        seat_ids.append(seat_id)
        # print(f'{row_num=} {col_num=} {seat_id=}')
        coordinates.append((row_num, col_num))
    # print(coordinates)
    # coordinates.sort(key=lambda tup: tup[0])
    print(len(_get_missing_coordinates(coordinates)))
    return max(seat_ids)


def _calculate_seat_id(row_num, col_num):
    return (row_num * 8) + col_num


def _get_missing_coordinates(coordinates):
    missing = []
    begin = coordinates[0]
    end = coordinates[-1]
    print(f'{begin=} {end=}')
    current = [begin[0], begin[1]]
    while current[0] <= end[0]:
        while current[1] <= 7:
            # print(f'{current=}')
            if (current[0], current[1]) not in coordinates:
                missing.append(current)
            current[1] += 1
            # input("Press Enter to continue...")
        current[0] += 1
        current[1] = 0
        # print(f'{current=}')
    return missing
