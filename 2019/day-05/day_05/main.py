import copy


OPERATION_MAPPING = {
        1: lambda num1, num2: num1 + num2,
        2: lambda num1, num2: num1 * num2
}


def part1():
    data = get_input("input_day_02")
    data[1] = 12
    data[2] = 2

    for opcode, num1_pos, num2_pos, dest_pos in take_four(data):
        num1_val = data[num1_pos]
        num2_val = data[num2_pos]

        data[dest_pos] = OPERATION_MAPPING.get(opcode)(num1_val, num2_val)

    print(data[0])


def part2():
    print("part2")
    pass


def take_four(things):
    cur_pos = 0
    while things[cur_pos] != 99:
        yield things[cur_pos:cur_pos+4]
        cur_pos += 4


def get_input(input_file):
    with open(input_file, 'r') as fh:
        line = fh.readline().strip('\n')
        return [int(value) for value in line.split(",")]
