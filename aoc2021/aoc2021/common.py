def get_input(input_file):
    with open(input_file, 'r') as fh:
        return [int(line) for line in fh.readlines()]


def get_input_as_strings(input_file):
    with open(input_file, 'r') as fh:
        return [line.rstrip() for line in fh.readlines()]


def slice_list(slice_length, input_list):
    sliced_list = []
    max_index = len(input_list) - slice_length + 1
    for i in range(0, max_index):
        temp_list = []
        for r in range(i, i + slice_length):
            temp_list.append(input_list[r])
        sliced_list.append(temp_list)
    return sliced_list
