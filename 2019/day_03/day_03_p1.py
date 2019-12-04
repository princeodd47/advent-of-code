class StarMap:
    def __init__(self):
        self.origin = (0, 0)

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

    def get_segments(self, wires):
        moves = []
        wire_counter = 0
        for wire in wires:
            cur_pos = self.origin
            cur_wire_moves = []
            for move in wire:
                new_position = get_new_pos(cur_pos, move)
                cur_wire_moves.append((cur_pos, new_position))
                cur_pos = new_position
            moves.append(cur_wire_moves)
            wire_counter += 1
        return moves

    def get_points(self, segments):
        points = []
        # print(f"segments: {segments}")
        for segment in segments:
            # print(f"segment: {segment}")
            # points[move] = []
            # points[move] = self.get_points_between_segments(segment)
            # points.append(self.get_points_in_segments(segment))
            new_points = self.get_points_in_segments(segment)
            points = [*points, *new_points]
        return points

    def get_points_in_segments(self, segment):
        # print(segment)
        point_1_x = segment[0][0]
        point_1_y = segment[0][1]
        point_2_x = segment[1][0]
        point_2_y = segment[1][1]
        points = []
        # Did x change?
        # Did y change?
        # Which direction?
        if point_1_x == point_2_x:
            # y changed
            x = point_1_x
            if point_1_y < point_2_y:
                # positive change
                y_begin = point_1_y
                y_end = point_2_y
            else:
                # negative change
                y_begin = point_2_y
                y_end = point_1_y
            y = y_begin
            while y <= y_end:
                # do not add origin to segements
                if x != 0 and y != 0:
                    points.append((x,y))
                y += 1
        else:
            # x changed
            y = point_1_y
            if point_1_x < point_2_x:
                # positive change
                x_begin = point_1_x
                x_end = point_2_x
            else:
                # negative change
                x_begin = point_2_x
                x_end = point_1_x
            x = x_begin
            while x <= x_end:
                # do not add origin to segements
                if x != 0 and y != 0:
                    points.append((x,y))
                x += 1
        return points


def get_new_pos(position, move):
    """
    Arguments:
        position(int, int): (12, 14)
        move(str): R1001
    """
    # print(f"position:{position}")
    # print(f"move:{move}")
    direction = move[0]
    spaces = int(move[1:])
    switcher = {
        "L": move_left(position, spaces),
        "R": move_right(position, spaces),
        "U": move_up(position, spaces),
        "D": move_down(position, spaces)
    }
    return switcher.get(direction)


def move_left(position, spaces):
    x = position[0] - spaces
    y = position[1]
    new_position = (x, y)
    return new_position


def move_right(position, spaces):
    x = position[0] + spaces
    y = position[1]
    new_position = (x, y)
    return new_position


def move_up(position, spaces):
    x = position[0]
    y = position[1] + spaces
    new_position = (x, y)
    return new_position


def move_down(position, spaces):
    x = position[0]
    y = position[1] - spaces
    new_position = (x, y)
    return new_position


def find_intersections(line_1, line_2):
    set_1 = set(line_1)
    set_2 = set(line_2)
    if (set_1 & set_2):
        return(set_1 & set_2)
    else:
        print("no intersections found")


def find_distance_from_origin(point):
    distance = abs(point[0]) + abs(point[1])
    return distance


def find_shortest_distance(intersections):
    shortest_distance = 999999
    for intersection in intersections:
        distance = find_distance_from_origin(intersection)
        if distance < shortest_distance:
            shortest_distance = distance
    return shortest_distance


def main():
    starmap = StarMap()
    lines = starmap.get_input("input")
    wires = starmap.get_wires(lines)
    wires_segments = starmap.get_segments(wires)
    line_1_points = starmap.get_points(wires_segments[0])
    line_2_points = starmap.get_points(wires_segments[1])
    intersections = find_intersections(line_1_points, line_2_points)
    print(find_shortest_distance(intersections))
    # print(wires[0][0])
    # print(end_points[0])
    # print(moves["R8_U5"])


main()
