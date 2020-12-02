import itertools

from common.read_file import get_input


def part1():
    print(find_values_p1("input/day_01"))


def part2():
    print(find_values_p2("input/day_01"))


def find_values_p1(input_file):
    values = get_input(input_file)
    for a, b in itertools.combinations(values, 2):
        if a + b == 2020:
            product = a * b
            return f'{a=} {b=} {product=}'
    return f'not found'
    # a=1301 b=719 product=935419


def find_values_p2(input_file):
    values = get_input(input_file)
    for a, b, c in itertools.combinations(values, 3):
        if a + b + c == 2020:
            product = a * b * c
            return f'{a=} {b=} {c=} {product=}'
    return f'not found'
    # a=889 b=1079 c=52 product=49880012


def part2_brute_force():
    print(find_values_p2_brute_force("input/day_01"))


def part1_brute_force():
    print(find_values_p1_brute_force("input/day_01"))



def find_values_p1_brute_force(input_file):
    values = get_input(input_file)
    for value1 in values:
        for value2 in values:
            if value1 != value2:
                total = value1 + value2
                if total == 2020:
                    product = value1 * value2
                    return f'{value1=} {value2=} {product=}'
    return 'none found'
    # value1=1301 value2=719 product=935419


def find_values_p2_brute_force(input_file):
    values = get_input(input_file)
    for value1 in values:
        for value2 in values:
            for value3 in values:
                if (value1 != value2
                        and value1 != value3
                        and value2 != value3):
                    total = value1 + value2 + value3
                    if total == 2020:
                        product = value1 * value2 * value3
                        return f'{value1=} {value2=} {value3=} {product=}'

    return 'none found'
    # value1=889 value2=1079 value3=52 product=49880012
