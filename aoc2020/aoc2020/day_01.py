from .common import get_input


def part1():
    print(find_values_p1("input/day_01"))


def part2():
    print(find_values_p2("input/day_01"))


def find_values_p1(input_file):
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

def find_values_p2(input_file):
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
