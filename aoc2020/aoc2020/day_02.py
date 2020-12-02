import logging

from common.read_file import get_input_as_strings

logging.basicConfig(level=logging.CRITICAL)

class Password():
    def __init__(self, min_count, max_count, required_character, value):
        self.min_count = int(min_count)
        self.max_count = int(max_count)
        self.required_character = required_character
        self.value = value


def part1():
    print(get_acceptable_password_count_part1("input/day_02"))
    # answer: 620


def part2():
    print(get_acceptable_password_count_part2("input/day_02"))
    # answer: 727


def get_acceptable_password_count_part1(input_file):
    acceptable_password_count = 0
    values = get_input_as_strings(input_file)
    for value in values:
        password_obj = _format_input(value)
        if _meets_password_policy_part1(password_obj):
            acceptable_password_count += 1
    return acceptable_password_count


def get_acceptable_password_count_part2(input_file):
    acceptable_password_count = 0
    values = get_input_as_strings(input_file)
    for value in values:
        logging.debug(f'{value=}')
        password_obj = _format_input(value)
        if _meets_password_policy_part2(password_obj):
            acceptable_password_count += 1
    return acceptable_password_count


def _format_input(input_string):
    split_input = input_string.split()
    min_count, max_count = split_input[0].split('-')
    required_character = split_input[1].split(':')[0]
    password_value = split_input[2]
    password_obj = Password(min_count=min_count,
                            max_count=max_count,
                            required_character=required_character,
                            value=password_value)
    return password_obj


def _meets_password_policy_part1(password_obj):
    character_count = password_obj.value.count(password_obj.required_character)
    return password_obj.min_count <= character_count <= password_obj.max_count


def _meets_password_policy_part2(password_obj):
    criteria_1 = _character_exists_in_position(password_obj.value,
                                               password_obj.min_count-1,
                                               password_obj.required_character
                                               )
    criteria_2 = _character_exists_in_position(password_obj.value,
                                               password_obj.max_count-1,
                                               password_obj.required_character
                                               )
    return criteria_1 is not criteria_2


def _character_exists_in_position(password, position, character):
    if len(password) >= position and character == password[position]:
        return True
    return False
