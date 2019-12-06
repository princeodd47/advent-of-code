import copy


OPERATION_MAPPING = {
        1: lambda num1, num2: num1 + num2,
        2: lambda num1, num2: num1 * num2
}


def main_1():
    data = get_input("input_ex_1")
    cur_pos = 0
    while data[cur_pos] != 99:
        opcode = data[cur_pos]
        num1_pos = data[cur_pos + 1]
        num2_pos = data[cur_pos + 2]
        num1_val = data[num1_pos]
        num2_val = data[num2_pos]
        dest_pos = data[cur_pos + 3]

        data[dest_pos] = OPERATION_MAPPING.get(opcode)(num1_val, num2_val)
        cur_pos += 4

    print(data)


def problem_1():
    data = get_input("input")
    data[1] = 12
    data[2] = 2

    for opcode, num1_pos, num2_pos, dest_pos in take_four(data):
        num1_val = data[num1_pos]
        num2_val = data[num2_pos]

        data[dest_pos] = OPERATION_MAPPING.get(opcode)(num1_val, num2_val)

    return data[0]


def problem_2():
    data = get_input("input")
    data_backup = copy.copy(data)

    for noun in range(0, 100):
        for verb in range(0, 100):
            data[1] = noun
            data[2] = verb
            for opcode, num1_pos, num2_pos, dest_pos in take_four(data):
                num1_val = data[num1_pos]
                num2_val = data[num2_pos]

                data[dest_pos] = OPERATION_MAPPING.get(opcode)(num1_val, num2_val)

            if data[0] == 19690720:
                return 100 * data[1] + data[2]

            data = copy.copy(data_backup)


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
    print(f"{problem_1()=}")
    print(f"{problem_2()=}")
