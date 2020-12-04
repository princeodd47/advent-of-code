from common.read_file import get_input_as_strings


def part1():
    print(_get_valid_passport_count('input/day_03'))


def part2():
    print(_get_valid_passport_count('input/day_04'))


def _get_valid_passport_count(input_file):
    # passports = _parse_passports(input_file)
    return 'foo'

def _parse_passports(input_file):
    passports = []
    lines = get_input_as_strings(input_file)
    for line in lines:
        _do_the_thing()
    return passports


def _do_the_thing():
    print('foo')
