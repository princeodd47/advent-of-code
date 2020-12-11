from common.read_file import get_input_as_strings


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
    print(_do_second_thing("input/day_08"))


def _do_first_thing(input_file):
    input_content = _parse_input(input_file)
    # print(f'{input_content=}')
    jolt_difference = JoltDifference(input_content)
    differences = jolt_difference._get_jolt_difference_counts()
    jolt_difference.print_difference_counts()
    return differences[1] * differences[3]


def _do_second_thing(input_file):
    input_content = _parse_input(input_file)
    return 0


def _parse_input(input_file):
    lines = get_input_as_strings(input_file)
    parsed_lines = []
    for line in lines:
        parsed_lines.append(int(line))
    parsed_lines.sort()
    return parsed_lines


def _get_jolt_difference(input_content):
    return 0
