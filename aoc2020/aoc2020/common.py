def get_input(input_file):
    with open(input_file, 'r') as fh:
        return [int(line) for line in fh.readlines()]


def get_input_as_strings(input_file):
    with open(input_file, 'r') as fh:
        return [line.rstrip() for line in fh.readlines()]
