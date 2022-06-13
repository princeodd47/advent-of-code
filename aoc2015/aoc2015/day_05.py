from . import common


def part1():
    strings = common.get_input_as_strings("input/day_05")
    nice_strings = []
    naughty_strings = []
    for s in strings:
        if _get_classification_part1(s) == "nice":
            nice_strings.append(s)
        else:
            naughty_strings.append(s)
    print(len(nice_strings))
    # answer: 238


def _get_classification_part1(string):
    if _is_nice_part1(string):
        return "nice"
    return "naughty"


def _is_nice_part1(string):
    if (_contains_required_number_of_vowels(string, 3)
    and _contains_consecutive_duplicates(string)
    and not _contains_illegal_stings(string)):
        return True
    return False


def _contains_required_number_of_vowels(string, required_vowel_count):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0
    for v in vowels:
        count = string.count(v)
        vowel_count += count
    return vowel_count >= required_vowel_count


def _contains_consecutive_duplicates(string):
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            return True
    return False


def _contains_illegal_stings(string):
    illegal_strings = ['ab', 'cd', 'pq', 'xy']
    if any(illegal_string in string for illegal_string in illegal_strings):
        return True
    return False
