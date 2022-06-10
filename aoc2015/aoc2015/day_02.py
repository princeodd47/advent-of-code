from . import common

from itertools import combinations
import math


def part1():
    input_dimensions = common.get_input_as_strings("input/day_02")
    total_amount = 0
    for d in input_dimensions:
        total_amount += _calculate_amount(d)
    print(total_amount)


def _calculate_amount(dimensions):
    values = _sanitize_input(dimensions)
    comb = combinations(values, 2)

    total_amount = 0
    amounts = []

    for i in list(comb):
        amount = i[0] * i[1]
        amounts.append(amount)

    extra = min(amounts)

    for a in amounts:
        total_amount += 2 * a
    total_amount += extra

    return total_amount


def _list_of_str_to_int(input_list):
    return [int(i) for i in input_list]


def _sanitize_input(input_line):
    values = input_line.split("x")
    int_values = _list_of_str_to_int(values)
    return int_values


def part2():
    input_dimensions = common.get_input_as_strings("input/day_02")
    total_amount = 0
    for d in input_dimensions:
        total_amount += _calculate_ribbon(d)
    print(total_amount)


def _calculate_ribbon(dimensions):
    values = _sanitize_input(dimensions)
    total_amount = 0

    present_ribbon = _calculate_ribbon_for_present(values)
    total_amount += present_ribbon

    bow_ribbon = _calculate_ribbon_for_bow(values)
    total_amount += bow_ribbon

    return total_amount


def _calculate_ribbon_for_present(values):
    values.sort()
    return 2*values[0]+2*values[1]


def _calculate_ribbon_for_bow(values):
    return math.prod(values)
