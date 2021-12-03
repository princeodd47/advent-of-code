import collections

from . import common


def part1():
    print(find_values_p1("input/day_03"))
    # answer: 2498354


def part2():
    print(find_values_p2("input/day_03"))
    # answer: 3277956


def find_values_p1(input_file):
    input_values = common.get_input_as_strings(input_file)
    g,e = _get_binaries(input_values)
    gamma_rate = common.binary_to_decimal(''.join(g))
    epsilon_rate = common.binary_to_decimal(''.join(e))
    return gamma_rate * epsilon_rate


def _get_binaries(input_data):
    restruct = common.invert_matrix(input_data)
    gamma_rate_binary = []
    epsilon_rate_binary = []
    for r in restruct:
        most_common, least_common = _get_frequent_items(r)
        gamma_rate_binary.append(most_common)
        epsilon_rate_binary.append(least_common)
    return gamma_rate_binary, epsilon_rate_binary


def _get_frequent_items(item):
    most_common = collections.Counter(item).most_common()[0]
    least_common = collections.Counter(item).most_common()[-1]
    return most_common, least_common


def _get_item_count(item):
    return collections.Counter(item).most_common()


def find_values_p2(input_file):
    input_data= common.get_input_as_strings(input_file)
    o = _get_binaries_o_c(input_data, "most", 1)
    # print(f'{o=}')
    c = _get_binaries_o_c(input_data, "least", 0)
    # print(f'{c=}')
    oxygen_generator_rating = common.binary_to_decimal(''.join(o))
    # print(f'{oxygen_generator_rating=}')
    co2_scrubber_rating = common.binary_to_decimal(''.join(c))
    # print(f'{co2_scrubber_rating=}')
    return oxygen_generator_rating * co2_scrubber_rating
    # return 0


def _get_binaries_o_c(input_values, frequency, default):
    good_binaries = input_values.copy()
    position = 0
    while len(good_binaries) > 1:
        bad_binaries = []
        # print(f'{good_binaries=}')
        inverted_data = common.invert_matrix(good_binaries)
        # print(f'{inverted_data[position]=}')
        target = _get_target(inverted_data[position], frequency, default)
        for binary in good_binaries:
            # print(f'{position=} {target=}')
            # print(f'{binary=} {binary[position]=}')
            if binary[position] != target:
                # print(f'adding bad binary {binary=}')
                bad_binaries.append(binary)
        for bad_binary in bad_binaries:
            # print(f'{bad_binary=}')
            good_binaries.remove(bad_binary)
        position += 1
    # print(f'{good_binaries=}')
    return good_binaries


def _get_target(items, frequency, default):
    item_count = _get_item_count(items)
    # print(f'{item_count=}')
    most_common = item_count[0]
    least_common = item_count[1]
    if most_common[1] == least_common[1]:
        target = str(default)
    elif frequency == "most":
        target = most_common[0]
    else:
        target = least_common[0]
    return target


# def _get_binaries_o_c(input_values, frequency, default):
#     good_binaries = input_values.copy()
#     bad_binaries = []
#     # print(f'{good_binaries=}')
#     inverted_data = common.invert_matrix(good_binaries)
#     # print(inverted_data)
#     position = 0
#     for i in inverted_data:
#         # print(''.join(i))
#         most_common, least_common = _get_frequent_items(i)
#         if most_common == least_common:
#             target = default
#         elif frequency == "most":
#             target = most_common
#         else:
#             target = least_common
#         # print(f'{position=} {target=}')
#         for binary in good_binaries:
#             if len(good_binaries) > 1:
#                 # print(f'{binary=}')
#                 if binary[position] != target:
#                     # print(f'removing {binary=}')
#                     bad_binaries.append(binary)
#         for binary in bad_binaries:
#             good_binaries.remove(binary)
#         bad_binaries = []
#         position += 1
#         print(f'{good_binaries=}')
#     return good_binaries
