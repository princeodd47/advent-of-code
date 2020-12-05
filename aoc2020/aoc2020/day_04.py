import re

from tabulate import tabulate

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
        self.hcl_string = None

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
                if self.hcl:
                    self.hcl_string = self.hcl[1:]
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
        if self.byr:
            byr_int = int(self.byr)
        else:
            byr_int = 0
        conditions = [
            self.byr,
            1920 <= byr_int <= 2002
        ]
        return all(conditions)

    def valid_iyr(self):
        if self.iyr:
            iyr_int = int(self.iyr)
        else:
            iyr_int = 0
        conditions = [
            self.iyr,
            2010 <= iyr_int <= 2020
        ]
        return all(conditions)

    def valid_eyr(self):
        if self.eyr:
            eyr_int = int(self.eyr)
        else:
            eyr_int = 0
        conditions = [
            self.eyr,
            2020 <= eyr_int <= 2030
        ]
        return all(conditions)

    def valid_hgt(self):
        if not self.hgt or len(self.hgt) <= 3:
            return False
        value_format = self.hgt[-2:]
        length = len(self.hgt)
        value = int(self.hgt[:length -2])
        if value_format == 'cm':
            return 150 <= value <= 193
        if value_format == 'in':
            return 59 <= value <= 76
        return False

    def valid_hcl(self):
        if not self.hcl or self.hcl[0] != '#' or len(self.hcl_string) != 6:
            return False
        return self._hcl_contains_valid_characters()

    def _hcl_contains_valid_characters(self):
        valid_characters = re.compile(r'[^a-f0-9]')
        string = valid_characters.search(self.hcl_string)
        return not bool(string)

    def valid_ecl(self):
        valid_colors = [
            "amb",
            "blu",
            "brn",
            "gry",
            "grn",
            "hzl",
            "oth"
        ]
        if self.ecl and self.ecl in valid_colors:
            return True
        return False

    def valid_pid(self):
        if not self.pid:
            return False
        conditions = [
            len(self.pid) == 9,
            self._pid_contains_valid_characters()
        ]
        return all(conditions)

    def _pid_contains_valid_characters(self):
        valid_characters = re.compile(r'[^0-9]')
        string = valid_characters.search(self.pid)
        return not bool(string)

    def print_debug(self):
        print(f'{self.byr=} {self.valid_byr()=} {self.iyr=} {self.valid_iyr()=} {self.eyr=} {self.valid_eyr()=} {self.hgt=} {self.valid_hgt()=} {self.hcl=} {self.valid_hcl()=} {self.ecl=} {self.valid_ecl()=} {self.pid=} {self.valid_pid()=}')

    def print_passport(self, count):
        # print(f'byr:{self.byr} iyr:{self.iyr} eyr:{self.eyr} hgt:{self.hgt} hcl:{self.hcl} ecl:{self.ecl} pid:{self.pid} cid:{self.cid}')
        pid = f'{self.pid} {len(self.pid)}'
        data = [[count, self.byr, self.iyr, self.eyr, self.hgt, self.hcl, self.ecl, pid]]
        headers = ['#', 'byr:1920-2002', 'iyr:2010-2020', 'eyr:2020-2030', 'hgt:150-193cm/59-76in', 'hcl:# 6dig hex', 'ecl:3 char', 'pid:9 dig']
        print(tabulate(data, headers))


def part1():
    print(_get_valid_passport_count('input/day_04'))
    # answer: 196


def part2():
    print(_get_valid_passport_count('input/day_04'))
    # answer: 114


def _get_valid_passport_count(input_file):
    passports = _parse_passports(input_file)
    valid_passport_count = 0
    for passport in passports:
        if passport.is_valid():
            valid_passport_count += 1
            # if valid_passport_count >= 27:
            #     passport.print_passport(valid_passport_count)
            #     input("Press Enter to continue...")
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
