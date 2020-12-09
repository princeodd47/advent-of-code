import itertools

from common.read_file import get_input


class XmasCypher():
    def __init__(self, cypher_input, group_count):
        self._group_count = group_count
        self._group = cypher_input[:group_count]
        self._cypher = cypher_input[group_count:]

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


def part1():
    group_count = 25
    print(_find_incorrect_number("input/day_09", group_count))


def part2():
    print(_do_second_thing("input/day_09"))


def _find_incorrect_number(input_file, group_count):
    cypher = XmasCypher(_parse_input(input_file), group_count)
    bad_num = cypher.decrypt()
    return bad_num


def _do_second_thing(input_file):
    input_content = _parse_input(input_file)
    return len(input_content)


def _parse_input(input_file):
    lines = get_input(input_file)
    parsed_lines = []
    for line in lines:
        parsed_lines.append(int(line))
    return parsed_lines
