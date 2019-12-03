class StarMap:
    def __init__(self):
        self.origin = "R0"
        self.cur_pos = self.origin

    def get_input(self, input_file):
        with open(input_file, 'r') as fh:
            lines = []
            line = fh.readline()
            while line:
                split_line = line.split('\n')
                lines.append(split_line[0])
                line = fh.readline()
        return lines

    def get_wires(self, lines):
        moves = []
        for line in lines:
            moves.append(line.split(","))
        return moves

    def get_end_points(self, wires):
        moves = []
        wire_counter = 0
        for wire in wires:
            previous = self.origin
            cur_wire_moves = []
            for move in wire:
                cur_wire_moves.append((previous, move))
                previous = move
            moves.append(cur_wire_moves)
            wire_counter += 1
        return moves

    def get_moves(self, end_points):
        moves = []
        for end_point in end_points:
            move = f"{end_point[0]}_{end_point[1]}"
            moves[move] = []
            moves[move] = self.get_moves_in_end_points(end_point)
        return moves

    def get_moves_in_end_points(self, end_point):
        raise NotImplementedError

    def update_cur_pos(self, move):
        direction = move[0]
        spaces = move[1:]
        switcher = {
            "L": self.move_left(spaces),
            "R": self.move_right(spaces),
            "U": self.move_up(spaces),
            "D": self.move_down(spaces)
        }
        switcher.get(direction)

    def move_left(self, spaces):
        self.cur_pos[0] -= spaces

    def move_right(self, spaces):
        self.cur_pos[0] += spaces

    def move_up(self, spaces):
        self.cur_pos[1] += spaces

    def move_down(self, spaces):
        self.cur_pos[1] -= spaces


def main():
    starmap = StarMap()
    lines = starmap.get_input('input_small')
    wires = starmap.get_wires(lines)
    end_points = starmap.get_end_points(wires)
    # TODO: Update end_points to be position tuples.
    # moves = starmap.get_moves(end_points)
    print(wires[0][0])
    print(end_points[0])
    # print(moves["R8_U5"])


main()
