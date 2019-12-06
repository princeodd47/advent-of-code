def addition(num1, num2):
    return num1 + num2


def multiplication(num1, num2):
    return num1 * num2


OPERATION_MAPPING = {
        1: lambda num1, num2: num1 + num2,
        2: lambda num1, num2: num1 * num2
}


def main_1():
    data = get_input("input_ex_1")

    #cur_pos = 0
    #while data[cur_pos] != 99:
    for opcode, num1_pos, num2_pos, dest_pos in take_four(data):
        #opcode = data[cur_pos]
        #opcode, num1_pos, num2_pos, dest_pos = data[cur_pos:cur_pos+4]
        #num1_pos = data[cur_pos + 1]
        #num2_pos = data[cur_pos + 2]
        num1_val = data[num1_pos]
        num2_val = data[num2_pos]
        #dest_pos = data[cur_pos + 3]

        data[dest_pos] = OPERATION_MAPPING.get(opcode)(num1_val, num2_val)
        #cur_pos += 4

    print(data)


def main():
    data = get_input("input_ex_1")

    for opcode, num1_pos, num2_pos, dest_pos in take_four(data):
        num1_val = data[num1_pos]
        num2_val = data[num2_pos]

        data[dest_pos] = OPERATION_MAPPING.get(opcode)(num1_val, num2_val)

    print(data)


def take_four(things):
    cur_pos = 0
    while things[cur_pos] != 99:
        yield things[cur_pos:cur_pos+4]
        cur_pos += 4


def get_input(input_file):
    with open(input_file, 'r') as fh:
        line = fh.readline().strip('\n')
        return [int(value) for value in line.split(",")]


if __name__ == "__main__":
    main()
