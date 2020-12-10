import itertools
import sys

from common.read_file import get_input


class XmasCypher():
    def __init__(self, cypher_input, group_count):
        self._group_count = group_count
        self._group = cypher_input[:group_count]
        self._cypher = cypher_input[group_count:]
        self._cypher_input = cypher_input

    def print(self):
        print(f'{self._group=}')
        print(f'{self._cypher=}')

    def decrypt(self):
        while self._cypher:
            if not self._check_sum():
                return self._cypher[0]
            self._advance()
        return 0

    def _check_sum(self):
        for c in itertools.combinations(self._group, 2):
            if c[0] != c[1] and c[0] + c[1] == self._cypher[0]:
                return True
        return False

    def _advance(self):
        self._group = self._group[1:]
        self._group.append(self._cypher[0])
        self._cypher = self._cypher[1:]

    def _advance_cypher_input(self):
        self._cypher_input = self._cypher_input[1:]
        # print(f'len={len(self._cypher_input)} begin={self._cypher_input[1:]}')
        # input("Press Enter to continue...")

    def _find_sequence(self, target_num):
        total = 0
        while total != target_num:
            sequence = self._add_until_target_num(target_num)
            total = sum(sequence)
            # print(f'{total=}')
            if total == target_num:
                # print('sequence found!')
                # print(f'{sequence=}')
                min_plus_max = min(sequence) + max(sequence)
                return min_plus_max
            self._advance_cypher_input()
        return 0

    def _add_until_target_num(self, target_num):
        # print('_add_until_target_num() called')
        total = 0
        sequence = []
        for i in self._cypher_input:
            total += i
            sequence.append(i)
            # print(f'{sequence=}')
            # print(f'{total=}')
            if total >= target_num:
                return sequence


def part1():
    group_count = 25
    print(_find_incorrect_number("input/day_09", group_count))
    # answer: 85848519


def part2():
    print(_find_sequence("input/day_09"))


def _find_incorrect_number(input_file, group_count):
    cypher = XmasCypher(_parse_input(input_file), group_count)
    bad_num = cypher.decrypt()
    return bad_num


def _find_sequence(input_file):
    target_num = 85848519
    # target_num = 127
    cypher = XmasCypher(_parse_input(input_file), 0)
    sequence = cypher._find_sequence(target_num)
    return sequence


def _parse_input(input_file):
    lines = get_input(input_file)
    parsed_lines = []
    for line in lines:
        parsed_lines.append(int(line))
    return parsed_lines
