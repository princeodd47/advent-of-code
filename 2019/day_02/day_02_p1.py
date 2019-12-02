class IntCode():
    def __init__(self):
        self.cur_pos = 0
        self.int_1 = 1
        self.int_2 = 2
        self.dest = 3
        self.input = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        # self.input = [
        #     1, 12, 2, 3,
        #     1, 1, 2, 3,
        #     1, 3, 4, 3,
        #     1, 5, 0, 3,
        #     2, 13, 1, 19,
        #     1, 19, 10, 23,
        #     1, 23, 6, 27,
        #     1, 6, 27, 31,
        #     1, 13, 31, 35,
        #     1, 13, 35, 39,
        #     1, 39, 13, 43,
        #     2, 43, 9, 47,
        #     2, 6, 47, 51,
        #     1, 51, 9, 55,
        #     1, 55, 9, 59,
        #     1, 59, 6, 63,
        #     1, 9, 63, 67,
        #     2, 67, 10, 71,
        #     2, 71, 13, 75,
        #     1, 10, 75, 79,
        #     2, 10, 79, 83,
        #     1, 83, 6, 87,
        #     2, 87, 10, 91,
        #     1, 91, 6, 95,
        #     1, 95, 13, 99,
        #     1, 99, 13, 103,
        #     2, 103, 9, 107,
        #     2, 107, 10, 111,
        #     1, 5, 111, 115,
        #     2, 115, 9, 119,
        #     1, 5, 119, 123,
        #     1, 123, 9, 127,
        #     1, 127, 2, 131,
        #     1, 5, 131, 0,
        #     99, 2, 0, 14, 0
        # ]

    def print_pos(self):
        if self.input[self.cur_pos] == 1:
            operation = '+'
            total = self.input[self.int_1] + self.input[self.int_2]
        else:
            operation = '*'
            total = self.input[self.int_1] * self.input[self.int_2]
        print(f"{self.cur_pos}:{self.input[self.cur_pos]}, "
              f"{self.int_1}:{self.input[self.int_1]}, "
              f"{self.int_2}:{self.input[self.int_2]}, "
              f"{self.dest}:{self.input[self.dest]}, "
              f"{self.input[self.dest]} = {self.input[self.int_1]}"
              f" {operation} {self.input[self.int_2]} = {total}"
         )

    def get_next_block(self):
        self.cur_pos += 4
        self.int_1 = self.cur_pos + 1
        self.int_2 = self.cur_pos + 2
        self.dest = self.cur_pos + 3

    def update(self, cur_pos, int_1, int_2, dest):
        cur_pos_val = self.input[cur_pos]
        int_1_val = self.input[int_1]
        int_2_val = self.input[int_2]
        dest_val = self.input[dest]

        if cur_pos_val == 1:
            self.input[dest_val] = self.input[int_1_val] + self.input[int_2_val]
        elif cur_pos_val == 2:
            self.input[dest_val] = self.input[int_1_val] * self.input[int_2_val]
        else:
            print(f"bad cur_pos: {self.cur_pos}")

    def calculate(self):
        # self.print_pos()
        if self.input[self.cur_pos] == 99:
            return self.input[0]
        self.update(self.cur_pos, self.int_1, self.int_2, self.dest)
        self.get_next_block()
        return self.calculate()


def main():
    intcode = IntCode()
    value = intcode.calculate()
    print(value)


main()
