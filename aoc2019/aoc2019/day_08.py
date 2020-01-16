from collections import deque
from enum import IntEnum

from aoc2019 import common


# class Color(IntEnum):
#     BLACK = '\u2588'
#     WHITE = ' '


def part1():
    # print(decode(width=3, length=2, input_file="input/day_08_p1_ex1"))
    decoded_data = decode()
    least_zeroes = {'layer': None, 'count': 99999}
    for layer in decoded_data:
        count = get_count_in_layer(layer, 0)
        if least_zeroes['count'] > count:
            least_zeroes['layer'] = layer
            least_zeroes['count'] = count
    one_count = get_count_in_layer(least_zeroes['layer'], 1)
    two_count = get_count_in_layer(least_zeroes['layer'], 2)
    print(one_count * two_count)
    return one_count * two_count


def part2():
    decoded_data = decode()
    image = []
    length = 6
    width = 25
    for row in range(length):
        image.append([])
        for col in range(width):
            image[row].append(get_pixel_value(decoded_data, row, col))
    print_image(image)


def get_pixel_value(decoded_data, row, col):
    return next(layer[row][col] for layer in decoded_data if layer[row][col] != 2)


def print_image(image):
    length = 6
    width = 25
    for row in range(length):
        for col in range(width):
            if image[row][col] == 0:
                print('\u2588', end='')
            if image[row][col] == 1:
                print(' ', end='')
        print("\n", end='')

def get_count_in_layer(layer, num):
    count = 0
    for row in layer:
        count += row.count(num)
    return count

def decode(width=25, length=6, input_file="input/day_08"):
    data_decode = []
    data = common.get_input_as_strings(input_file)
    data_deque = deque(data[0])
    i = 0
    while data_deque:
        data_decode.append([])
        for j in range(length):
            data_decode[i].append([])
            for k in range(width):
                data_decode[i][j].append(int(data_deque.popleft()))
        i = i + 1
    return data_decode
