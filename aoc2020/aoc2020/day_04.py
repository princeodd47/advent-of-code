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
        conditions = [
            self.valid_byr(),
            self.valid_iyr(),
            self.valid_eyr(),
            self.valid_hgt(),
            self.valid_hcl(),
            self.valid_ecl(),
            self.valid_pid()
        ]
        return all(conditions)

    def valid_byr(self):
        if self.byr is None:
            return False
        return True

    def valid_iyr(self):
        if self.iyr is None:
            return False
        return True

    def valid_eyr(self):
        if self.eyr is None:
            return False
        return True

    def valid_hgt(self):
        if self.hgt is None:
            return False
        return True

    def valid_hcl(self):
        if self.hcl is None:
            return False
        return True

    def valid_ecl(self):
        if self.ecl is None:
            return False
        return True

    def valid_pid(self):
        if self.pid is None:
            return False
        return True


def part1():
    optional_keys = ['cid']
    print(_get_valid_passport_count('input/day_04'))
    # answer: 196


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
