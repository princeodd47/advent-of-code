def get_file(in_file_name):
    with open(in_file_name) as in_file:
        data = in_file.readlines()
    return data

def write_str_to_file(in_str, out_file_name):
    with open(out_file_name, 'w') as out_file:
        out_file.write("{}\n".format(in_str))

data = get_file("input_small.txt")
polymers = list(data[0].rstrip())
print(polymers)
polymers_str = ''.join(polymers)
print(polymers_str)
write_str_to_file(polymers_str, "test_output")
