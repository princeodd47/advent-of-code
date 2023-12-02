from . import common

import re


def part1():
    print(find_values_p1("input/day_01"))
    # answer: 55386

def part2():
    print(find_values_p2("input/day_01"))
    # answer: 

def find_values_p1(input_file):
    values = common.get_input_as_strings(input_file)
    integers = []
    for value in values:
        integer_list = get_first_and_last_int(value)
        target_integer = int(f"{integer_list[0]}{integer_list[-1]}")
        integers.append(target_integer)
    return sum(integers)
    # print(integers)
    # return 0

def get_first_and_last_int(input_string):
    integers = re.findall(r'\d', input_string)
    return integers

def find_values_p2(input_file):
    values = common.get_input_as_string(input_file)
    return "p2 runs"
