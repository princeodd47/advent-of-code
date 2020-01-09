def get_good_num_count(begin, end):
    good_num_count = 0
    for num in range(begin, end):
        if has_seq_dupes(num) and always_increasing(num):
            good_num_count += 1
    return(good_num_count)


def has_seq_dupes(num):
    prev_digit = 10
    for digit in str(num):
        if int(digit) == prev_digit:
            return True
        prev_digit = int(digit)
    return False


def always_increasing(num):
    prev_digit = -1
    for digit in str(num):
        if int(digit) < prev_digit:
            return False
        prev_digit = int(digit)
    return True


def get_repitition_length(string):
    first_dig = string[0]
    return next((pos for pos, digit in enumerate(string) if digit != first_dig), len(string))


def is_good_number(string, has_pair=False):
    if not string:
        return True, has_pair
    length = get_repitition_length(string)
    has_pair = has_pair or length == 2
    if len(string) > length and string[0] > string[length]:
        return False, has_pair
    return is_good_number(string[length:], has_pair)


def is_gooder_number(number):
    goodness, has_pair = is_good_number(str(number))
    return goodness and has_pair


def get_good_num_count_p2(begin, end):
    return len([True for num in range(begin, end + 1) if is_gooder_number(num)])


def part1():
    begin = 130254
    end = 678275
    return get_good_num_count(begin, end)


def part2():
    begin = 130254
    end = 678275
    return get_good_num_count_p2(begin, end)
