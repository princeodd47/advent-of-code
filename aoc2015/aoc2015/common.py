def get_input(input_file):
    with open(input_file, 'r') as fh:
        return [int(line) for line in fh.readlines()]


def get_input_as_strings(input_file):
    with open(input_file, 'r') as fh:
        return [line.rstrip() for line in fh.readlines()]


def get_input_as_single_string(input_file):
    with open(input_file, 'r') as fh:
        return [line.rstrip() for line in fh.readlines()][0]


def slice_list(slice_length, input_list):
    sliced_list = []
    max_index = len(input_list) - slice_length + 1
    for i in range(0, max_index):
        temp_list = []
        for r in range(i, i + slice_length):
            temp_list.append(input_list[r])
        sliced_list.append(temp_list)
    return sliced_list


def invert_matrix(input_data):
    line_length = len(input_data[0])
    cols = []
    for i in range(line_length):
        col = []
        for value in input_data:
            col.append(value[i])
        cols.append(col)
    return cols


def binary_to_decimal(binary):
    return int(binary, 2)
