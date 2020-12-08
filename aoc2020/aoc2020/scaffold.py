from common.read_file import get_input_as_strings


def part1():
    print(_do_first_thing("input/day_08"))


def part2():
    print(_do_second_thing("input/day_08"))


def _do_first_thing(input_file):
    input_content = _parse_input(input_file)
    return 0


def _do_second_thing(input_file):
    input_content = _parse_input(input_file)
    return 0


def _parse_input(input_file):
    lines = get_input_as_strings(input_file)
    parsed_lines = []
    for line in lines:
        parsed_lines.append(line)
    return parsed_lines
