import ast

from common.read_file import get_input_as_strings


class Passport():
    def __init__(self, dictionary):
        self.byr = None
        self.iyr = None
        self.eyr = None
        self.hgt = None
        self.hcl = None
        self.ecl = None
        self.pid = None
        self.cid = None
        for key, value in dictionary.items():
            if key == "byr":
                self.byr = value
            if key == "iyr":
                self.iyr = value
            if key == "eyr":
                self.eyr = value
            if key == "hgt":
                self.hgt = value
            if key == "hcl":
                self.hcl = value
            if key == "ecl":
                self.ecl = value
            if key == "pid":
                self.pid = value
            if key == "cid":
                self.cid = value

    def is_valid(self):
        if (self.byr is not None
                and self.iyr is not None
                and self.eyr is not None
                and self.hgt is not None
                and self.hcl is not None
                and self.ecl is not None
                and self.pid is not None):
            return True
        return False

def part1():
    optional_keys = ['cid']
    print(_get_valid_passport_count('input/day_04'))


def part2():
    _get_valid_passport_count('input/day_04_ex')


def _get_valid_passport_count(input_file):
    passports = _parse_passports(input_file)
    valid_passport_count = 0
    for passport in passports:
        if passport.is_valid():
            valid_passport_count += 1
    return valid_passport_count


def _parse_passports(input_file):
    passports = []
    lines = get_input_as_strings(input_file)
    passport = ''
    for line in lines:
        if line != '':
            if passport == '':
                passport = line
            else:
                passport += ' ' + line
        else:
            passport_obj = _create_passport_obj(passport)
            passports.append(passport_obj)
            passport = ''
    passport_obj = _create_passport_obj(passport)
    passports.append(passport_obj)
    return passports


def _string_to_dict(string):
    dictionary = {}
    kv_pairs = string.split(' ')
    for pair in kv_pairs:
        key, value = pair.split(':')
        dictionary[key] = value
    return dictionary


def _create_passport_obj(passport_string):
    passport_dictionary = _string_to_dict(passport_string)
    passport_obj = Passport(passport_dictionary)
    return passport_obj
