def get_input(input_file):
    data = []
    with open(input_file, 'r') as fh:
        line = fh.readline()
        while line:
            data.append(int(line))
            line = fh.readline()
    return data
