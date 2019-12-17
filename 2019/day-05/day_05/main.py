import logging
import pdb

logging.basicConfig(level=logging.CRITICAL)


def part1():
    test = IntCode()
    test.get_input("input")
    test.diagnostic_program(1)


def part2():
    # TODO: make all other methds private
    test = IntCode()
    test.get_input("input")
    test.diagnostic_program(5)
    print(test.result)


def sanitize_opcode(val):
    return str(val).zfill(5)


class IntCode():
    def __init__(self):
        # TODO: make variables private
        self._logger = logging.getLogger(__name__)
        self._is_running = False
        self.cur_index = 0
        self.system_id = 0
        # TODO: keep public
        self.data = []
        self.result_history = []

    @property
    def result(self):
        return self.result_history[-1]

    def get_operation(self, opcode):
        op_map = {
            "01": self.addition,
            "02": self.multiplication,
            "03": self.input,
            "04": self.output,
            "05": self.jump_if_true,
            "06": self.jump_if_false,
            "07": self.less_than,
            "08": self.equals,
            "99": self.halt
        }
        return op_map.get(opcode)

    def halt(self, opstring):
        self._is_running = False

    def get_input(self, input_file):
        with open(input_file, 'r') as fh:
            line = fh.readline().strip('\n')
            self.data = [int(value) for value in line.split(",")]

    def diagnostic_program(self, user_input):
        self._is_running = True
        self.system_id = user_input
        opstring = ""

        # self._logger.debug(self.data)
        # self.print_table_header()
        # self.print_table()

        while self._is_running:
            self._logger.debug(f"{self.cur_index=}")
            self._logger.debug(f"{self.data[self.cur_index]=}")
            opstring = sanitize_opcode(self.data[self.cur_index])
            opcode = opstring[-2:]

            operation = self.get_operation(opcode)
            operation(opstring)

            self._logger.debug("")
            # self._logger.debug(self.data)
            # self.print_table()
        return self.data[0]

    def get_value_from_data(self, index_val):
        if index_val < len(self.data) - 1:
            return int(self.data[index_val])
        else:
            return None

    def get_desired_index(self, param, mode):
        if mode == 0:
            return self.data[param]
        if mode == 1:
            return param
        raise Exception

    def increment_index(self, value):
        self.cur_index += value

    def addition(self, opstring):
        """Opcode 1 adds together numbers read from two positions and stores the result in a
        third position. The three integers immediately after the opcode tell you these three
        positions - the first two indicate the positions from which you should read the
        input values, and the third indicates the position at which the output should be
        stored.
        For example, if your Intcode computer encounters 1,10,20,30, it should read the
        values at positions 10 and 20, add those values, and then overwrite the value at
        position 30 with their sum."""
        param1 = self.get_value_from_data(self.cur_index + 1)
        param2 = self.get_value_from_data(self.cur_index + 2)
        param3 = self.get_value_from_data(self.cur_index + 3)

        param1_mode = int(opstring[2])
        param2_mode = int(opstring[1])

        param1_val = int(self.get_desired_index(param1, param1_mode))
        param2_val = int(self.get_desired_index(param2, param2_mode))

        self._logger.debug(f"add {self.cur_index=} {param1=} {param2=} {param3=} {param1_mode=} {param2_mode} {param1_val=} {param2_val=}")

        self.data[param3] = param1_val + param2_val
        self.increment_index(4)

    def multiplication(self, opstring):
        """Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead
        of adding them. Again, the three integers after the opcode indicate where the inputs
        and outputs are, not their values."""
        param1 = self.get_value_from_data(self.cur_index + 1)
        param2 = self.get_value_from_data(self.cur_index + 2)
        param3 = self.get_value_from_data(self.cur_index + 3)

        param1_mode = int(opstring[2])
        param2_mode = int(opstring[1])

        param1_val = int(self.get_desired_index(param1, param1_mode))
        param2_val = int(self.get_desired_index(param2, param2_mode))

        self._logger.debug(f"mult {self.cur_index=} {param1=} {param2=} {param3=} {param1_mode=} {param2_mode} {param1_val=} {param2_val=}")

        self.data[param3] = param1_val * param2_val
        self.increment_index(4)

    def input(self, opstring):
        """Opcode 3 takes a single integer as input and saves it to the
           position given by its only parameter.
           For example, the instruction 3,50 would take an input value and store it at
           address 50."""
        param1 = self.get_value_from_data(self.cur_index + 1)

        self._logger.debug(f"input {self.cur_index=} {param1=}")

        self.data[param1] = self.system_id
        self.increment_index(2)

    def output(self, opstring):
        """Opcode 4 outputs the value of its only parameter.
        For example, the instruction 4,50 would output the value at address 50."""
        param1 = self.get_value_from_data(self.cur_index + 1)
        param1_mode = int(opstring[2])
        param1_val = int(self.get_desired_index(param1, param1_mode))

        self._logger.debug(f"output {self.cur_index=} {param1=} {param1_mode=} {param1_val=}")

        self.result_history.append(param1_val)
        self.increment_index(2)

    def jump_if_true(self, opstring):
        """Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the
        instruction pointer to the value from the second parameter. Otherwise, it does
        nothing."""
        param1 = self.get_value_from_data(self.cur_index + 1)
        param1_mode = int(opstring[2])
        param1_val = int(self.get_desired_index(param1, param1_mode))

        self._logger.debug(f"jt p1 {self.cur_index=} {param1=} {param1_mode=} {param1_val=}")

        if param1_val != 0:
            param2 = self.get_value_from_data(self.cur_index + 2)
            param2_mode = int(opstring[1])
            param2_val = int(self.get_desired_index(param2, param2_mode))

            self._logger.debug(f"jt p2 {self.cur_index=} {param2=} {param2_mode=} {param2_val=}")

            self.cur_index = param2_val
        else:
            self.increment_index(3)

    def jump_if_false(self, opstring):
        """Opcode 6 is jump-if-false: if the first parameter is zero, it sets the
        instruction pointer to the value from the second parameter. Otherwise, it does
        nothing."""
        param1 = self.get_value_from_data(self.cur_index + 1)
        param1_mode = int(opstring[2])
        param1_val = int(self.get_desired_index(param1, param1_mode))

        self._logger.debug(f"jf p1 {self.cur_index=} {param1=} {param1_mode=} {param1_val=}")

        if param1_val == 0:
            param2 = self.get_value_from_data(self.cur_index + 2)
            param2_mode = int(opstring[1])
            param2_val = int(self.get_desired_index(param2, param2_mode))

            self._logger.debug(f"jf p2 {self.cur_index=} {param2=} {param2_mode=} {param2_val=}")

            self.cur_index = param2_val
        else:
            self.increment_index(3)


    def less_than(self, opstring):
        """Opcode 7 is less than: if the first parameter is less than the second parameter,
        it stores 1 in the position given by the third parameter. Otherwise, it stores 0."""
        param1 = self.get_value_from_data(self.cur_index + 1)
        param1_mode = int(opstring[2])
        param1_val = int(self.get_desired_index(param1, param1_mode))

        param2 = self.get_value_from_data(self.cur_index + 2)
        param2_mode = int(opstring[1])
        param2_val = int(self.get_desired_index(param2, param2_mode))

        param3 = self.get_value_from_data(self.cur_index + 3)

        self._logger.debug(f"lt {self.cur_index=} {param1=} {param2=} {param3=} {param1_mode=} {param2_mode} {param1_val=} {param2_val=}")

        if param1_val < param2_val:
            self.data[param3] = 1
        else:
            self.data[param3] = 0
        self.increment_index(4)

    def equals(self, opstring):
        """Opcode 8 is equals: if the first parameter is equal to the second parameter, it
        stores 1 in the position given by the third parameter. Otherwise, it stores 0."""
        param1 = self.get_value_from_data(self.cur_index + 1)
        param1_mode = int(opstring[2])
        param1_val = int(self.get_desired_index(param1, param1_mode))

        param2 = self.get_value_from_data(self.cur_index + 2)
        param2_mode = int(opstring[1])
        param2_val = int(self.get_desired_index(param2, param2_mode))

        param3 = self.get_value_from_data(self.cur_index + 3)

        self._logger.debug(f"eq {self.cur_index=} {param1=} {param2=} {param3=} {param1_mode=} {param2_mode} {param1_val=} {param2_val=}")

        if param1_val == param2_val:
            self.data[param3] = 1
        else:
            self.data[param3] = 0
        self.increment_index(4)

    def print_table_header(self):
        print("i".rjust(4), end=" | ")
        count = 5
        for i in range(len(self.data)):
            print(str(i).rjust(4), end=" | ")
            count += 6
        print("\n"+"="*count)

    def print_table(self):
        print(str(self.cur_index).rjust(3), end=" | ")
        for i in self.data:
            print(str(i).rjust(4), end=" | ")
        print()
