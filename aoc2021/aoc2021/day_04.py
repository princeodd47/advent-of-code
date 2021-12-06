from . import common


class Bingo():
    def __init__(self, input_board):
        self.board_total = 0
        self.final_ball = 0
        self.board = []
        self._parse_board(input_board)

    def _parse_board(self, input_board):
        for row in input_board:
            full_row = []
            for col in row.split(" "):
                if col != "":
                    cell = {"num": int(col), "match": False}
                    full_row.append(cell)
            self.board.append(full_row)

    def print_board(self):
        for row in self.board:
            print(row)
        print()

    def check_ball(self, ball):
        ball_found = False
        row_counter = 0
        for row in self.board:
            col_counter = 0
            for col in row:
                if col['num'] == ball:
                    self.board[row_counter][col_counter]['match'] = True
                    ball_found = True
                col_counter += 1
            row_counter += 1
        return ball_found

    def check_for_bingo(self, ball):
        horizontal_bingo = self._check_horizontal_bingo()
        vertical_bingo = self._check_vertical_bingo()
        conditions = [
                horizontal_bingo,
                vertical_bingo
        ]
        if any(conditions):
            self.final_ball = ball
            return True
        return False

    def _check_horizontal_bingo(self):
        row_match = []
        for row in self.board:
            for col in row:
                row_match.append(col['match'])
            if all(row_match):
                return True
            row_match = []
        return False

    def _check_vertical_bingo(self):
        col_match = []
        for col in range(len(self.board)):
            for row in self.board:
                col_match.append(row[col]['match'])
            if all(col_match):
                return True
            col_match = []
        return False

    def _get_sum_of_false(self):
        for row in self.board:
            for col in row:
                if not col['match']:
                    self.board_total += col['num']

    def get_total(self):
        self._get_sum_of_false()
        return self.board_total * self.final_ball


def part1():
    print(find_values_p1("input/day_04"))
    # answer: 2496


def part2():
    print(find_values_p2("input/day_04_example"))
    # answer: 


def find_values_p1(input_file):
    input_values = common.get_input_as_strings(input_file)
    bingo_balls = input_values[0].split(',')
    input_values.pop(0)

    boards = _populate_boards(input_values)

    winning_board = play_bingo(bingo_balls, boards)
    return winning_board.get_total()


def play_bingo(bingo_balls, boards):
    for ball in bingo_balls:
        for board in boards:
            if board.check_ball(int(ball)):
                if board.check_for_bingo(int(ball)):
                    return board
    return Bingo([])


def _print_boards(boards):
    for b in boards:
        b.print_board()


def _populate_boards(input_values):
    boards = []
    board = []
    for line in input_values:
        if line == "":
            if board:
                boards.append(Bingo(board))
                board = []
        else:
            board.append(line)
    # handle last board in file
    boards.append(Bingo(board))
    board = []
    return boards


def find_values_p2(input_file):
    input_values = common.get_input_as_strings(input_file)
    return 0
