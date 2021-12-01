from . import common


class Depth:
    def __init__(self):
        self.cur_depth = None
        self.pre_depth = None
        self.inc_count = 0

    def compare_depth(self, new_depth):
        if self.cur_depth and self.cur_depth < new_depth:
            self.inc_count += 1
        self.cur_depth = new_depth

    def compare_sliding_depths(self, window, depths):
        slices = common.slice_list(window, depths)
        for s in slices:
            self.compare_depth(sum(s))

def part1():
    print(find_values_p1("input/day_01"))
    # answer: 1477

def part2():
    print(find_values_p2("input/day_01"))
    # answer: 1523


def find_values_p1(input_file):
    values = common.get_input(input_file)
    depth = Depth()

    for value in values:
        depth.compare_depth(value)
    return depth.inc_count


def find_values_p2(input_file):
    values = common.get_input(input_file)
    depth = Depth()

    depth.compare_sliding_depths(3, values)
    return depth.inc_count
