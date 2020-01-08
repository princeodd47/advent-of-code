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

def main():
    begin = 130254
    end = 678275
    print(get_good_num_count(begin, end))


main()
