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


def main():
    begin = 130254
    end = 678275
    print(len([True for num in range(begin, end + 1) if is_gooder_number(num)]))


main()
