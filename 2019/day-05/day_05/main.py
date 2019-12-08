import sys


def part1():
    test = Test()
    test.diagnostic_program()


def part2():
    print("part2")
    pass


def sanitize_opcode(val):
    return str(val).zfill(5)


def get_input(input_file):
    with open(input_file, 'r') as fh:
        line = fh.readline().strip('\n')
        return [int(value) for value in line.split(",")]


def get_user_input():
    return int(input("Please enter the system id:"))


class Test():
    def __init__(self):
        self.cur_index = 0
        self.data = get_input("input")

    def diagnostic_program(self):
        self.system_id = int(get_user_input())
        opcode = ""

        while opcode != "00099":
            opcode = sanitize_opcode(self.data[self.cur_index])
            op_val = int(opcode[-2:])
            param_1_mode = int(opcode[2])
            param_2_mode = int(opcode[1])
            # print(f"{self.cur_index} {opcode} {op_val=} {param_1_mode=} {param_2_mode=}")
            if op_val == 1:
                if param_1_mode == 0: # position mode
                    num1_pos = self.data[self.cur_index + 1]
                    num1_val = self.data[num1_pos]
                    # print(f"{self.data[num1_pos]=}")
                else: # immediate mode
                    num1_val = self.data[self.cur_index + 1]

                if param_2_mode == 0: # position mode
                    num2_pos = self.data[self.cur_index + 2]
                    num2_val = self.data[num2_pos]
                else: # immediate mode
                    num2_val = self.data[self.cur_index + 2]


                dest_pos = self.data[self.cur_index + 3]
                self.addition(int(num1_val), int(num2_val), int(dest_pos))

            elif op_val == 2:
                if param_1_mode == 0: # position mode
                    num1_pos = self.data[self.cur_index + 1]
                    num1_val = self.data[num1_pos]
                else: # immediate mode
                    num1_val = self.data[self.cur_index + 1]

                if param_2_mode == 0: # position mode
                    num2_pos = self.data[self.cur_index + 2]
                    num2_val = self.data[num2_pos]
                else: # immediate mode
                    num2_val = self.data[self.cur_index + 2]


                dest_pos = self.data[self.cur_index + 3]
                self.multiplication(int(num1_val), int(num2_val), int(dest_pos))

            elif op_val == 3:
                dest_pos = self.data[self.cur_index + 1]
                self.replacement(int(dest_pos))

            elif op_val == 4:
                if param_1_mode == 0: # position mode
                    num1_pos = self.data[self.cur_index + 1]
                    num1_val = self.data[num1_pos]
                else: # immediate mode
                    num1_val = self.data[self.cur_index + 1]

                self.output(int(num1_val))

            elif op_val == 5:
                param_1 = self.data[self.cur_index + 1]
                param_2 = self.data[self.cur_index + 2]
                self.jump_if_true(param_1, param_2)

            elif op_val == 6:
                pass

            elif op_val == 7:
                pass

            elif op_val == 8:
                pass


    def get_next_index(opcode):
        pass

    def get_operation(self, opcode):
        op_val = int(opcode[-2:])
        # print(op_val)
        switcher = {
            1: self.addition(),
            2: self.multiplication(),
            3: self.replacement(),
            4: self.output(),
        }

        return switcher.get(op_val)

    def addition(self, num1, num2, dest_pos):
        # print(f"addition: {num1=} {num2=} {dest_pos=}")
        self.data[dest_pos] = num1 + num2
        self.cur_index += 4
        return "addition"

    def multiplication(self, num1, num2, dest_pos):
        # print(f"multiplication: {num1=} {num2=} {dest_pos=}")
        self.data[dest_pos] = num1 * num2
        self.cur_index += 4
        return "multiplication"

    def replacement(self, dest_pos):
        # print(f"replacement: {self.system_id=} {dest_pos=}")
        self.data[dest_pos] = self.system_id
        self.cur_index += 2
        return "replacement"

    def jump_if_true(self, param1, param2):
        if param1 != 0:
            self.cur_index = self.data[param2]

    def jump_if_false(self, param1, param2):
        if param1 == 0:
            self.cur_index = self.data[param2]

    def less_than(self, param1, param2, param3):
        if param1 < param2:
            self.data[param3] = 1
        else:
            self.data[param3] = 0

    def equals(self, param1, param2, param3):
        if param1 == param2:
            self.data[param3] = 1
        else:
            self.data[param3] = 0

    def output(self, num1):
        print(num1)
        self.cur_index += 2
        return "output"
