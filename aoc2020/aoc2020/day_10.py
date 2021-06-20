from typing import List

from .common import get_input_as_strings


memo_path_example = '''

{
    '1':
    [
        2,
        3,
        4
    ],
    '2': []
    '3': []
    '4': []
}
'''

# class Memo():
#     def __init__(self, end):
#         self.paths = []
#         self.starts = []
#         self.end = end

#     def add_start(self, start):
#         self.starts.append(start)

#     def path_exists(self, start):
#         return(start in self.paths)

#     def get_path(self, start):
#         return self.paths[start]

class Path():
    def __init__(self, path):
        self.start = start
        self.path = {path}

    @property
    def last(self):
        return max(self.path)


class JoltDifference():
    def __init__(self, adapter_input):
        self._cur_jolt = 0
        self.difference_counts = {}
        self._account_for_device_builtin_voltage()
        self.adapters = adapter_input

    def _account_for_device_builtin_voltage(self):
        self.difference_counts.update({3: 1})

    def _get_jolt_difference_counts(self):
        for a in self.adapters:
            jolt_difference = a - self._cur_jolt
            # print(f'{jolt_difference=} = {a=} - {self._cur_jolt=}')
            if jolt_difference not in self.difference_counts:
                self.difference_counts.update({jolt_difference: 1})
            else:
                self.difference_counts[jolt_difference] += 1
            self._cur_jolt = a
            # self.print_difference_counts()
        return self.difference_counts

    def _add_difference(self, difference, value):
        self.difference_counts[difference] += value

    def print_difference_counts(self):
        print(f'{self.difference_counts=}')


def part1():
    print(_do_first_thing("input/day_10"))


def part2():
    print(_do_second_thing("input/day_10_ex_1"))


def _do_first_thing(input_file: str):
    input_content = _parse_input(input_file)
    # print(f'{input_content=}')
    jolt_difference = JoltDifference(input_content)
    differences = jolt_difference._get_jolt_difference_counts()
    jolt_difference.print_difference_counts()
    return differences[1] * differences[3]


def _do_second_thing(input_file: str):
    input_content: set[int] = _parse_input(input_file)
    return input_content


def _parse_input(input_file: str) -> List[int]:
    lines: list[str] = get_input_as_strings(input_file)
    return sorted(list(map(int, lines)))
