class StarMap:
    def __init__(self):
        self.origin = (0, 0)
        self.wires_distance_to_points = []
        self.wires_distance_to_points.append([])
        self.wires_distance_to_points.append([])
        self.distance_travelled = 0
        self.cur_wire = 0

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
        segments = []
        for wire in wires:
            cur_pos = self.origin
            cur_wire_segments = []
            for segment in wire:
                new_position = get_new_pos(cur_pos, segment)
                cur_wire_segments.append((cur_pos, new_position))
                cur_pos = new_position
            segments.append(cur_wire_segments)
        return segments

    def get_points(self, wire, segments):
        self.distance_travelled = 0
        points = []
        for segment in segments:
            new_points = self.get_points_in_segment(wire, segment)
            points = [*points, *new_points]
        return points

    def get_points_in_segment(self, wire, segment):
        # start and end points are working how I want them to
        begin_point = segment[0]
        end_point = segment[1]
        point_1_x = begin_point[0]
        point_1_y = begin_point[1]
        point_2_x = end_point[0]
        point_2_y = end_point[1]
        points = []

        # debug = False
        # if segment[0] in ((0, 0), (75, 0)) and wire == 0:
        #     debug = True

        # if debug:
        #     print(f"wire: {wire} segement: {segment}")

        # Did x change?
        # Did y change?
        # Which direction?
        if point_1_x == point_2_x:
            # y changed
            x = point_1_x
            y_begin = point_1_y
            y_end = point_2_y
            if point_1_y < point_2_y:
                # positive change
                y = y_begin + 1
                while y <= y_end:
                    # do not add origin to segements
                    point = (x, y)
                    if point != begin_point:
                        self.distance_travelled +=1
                        points.append((x, y))
        #                 if debug:
        #                     print(f"\tpoint: ({x},{y}) distance_travelled: {self.distance_travelled}")
                        self.wires_distance_to_points[wire].append((x, y, self.distance_travelled))
                    y += 1
            else:
                # negative change
                y = y_begin - 1
                while y >= y_end:
                    # do not add origin to segements
                    point = (x, y)
                    if point != begin_point:
                        self.distance_travelled +=1
                        points.append((x, y))
        #                 if debug:
        #                     print(f"\tpoint: ({x},{y}) distance_travelled: {self.distance_travelled}")
                        self.wires_distance_to_points[wire].append((x, y, self.distance_travelled))
                    y -= 1
        else:
            # x changed
            y = point_1_y
            x_begin = point_1_x
            x_end = point_2_x
            if point_1_x < point_2_x:
                # positive change
                x = x_begin + 1
                while x <= x_end:
                    # do not add origin to segements
                    point = (x, y)
                    if point != begin_point:
                        self.distance_travelled +=1
                        points.append((x, y))
        #                 if debug:
        #                     print(f"\tpoint: ({x},{y}) distance_travelled: {self.distance_travelled}")
                        self.wires_distance_to_points[wire].append((x, y, self.distance_travelled))
                    x += 1
            else:
                # negative change
                x = x_begin - 1
                while x >= x_end:
                    # do not add origin to segements
                    point = (x, y)
                    if point != begin_point:
                        self.distance_travelled +=1
                        points.append((x, y))
        #                 if debug:
        #                     print(f"\tpoint: ({x},{y}) distance_travelled: {self.distance_travelled}")
                        self.wires_distance_to_points[wire].append((x, y, self.distance_travelled))
                    x -= 1
        return points

    def get_distances_to_point_on_wire(self, wire, point):
        distances = []
        x = point[0]
        y = point[1]
        for entry in self.wires_distance_to_points[wire]:
            if entry[0] == x and entry[1] == y:
                distances.append(entry[2])
        return distances

    def get_shortest_total_distance_to_point(self, point):
        shortest_distance = float("inf")
        # print(f"point: {point} distance: {self.get_distances_to_point_on_wire(0, point)}")
        for distance in self.get_distances_to_point_on_wire(0, point):
            # print(f"distance: {distance}")
            if distance < shortest_distance:
                shortest_distance = distance
        wire_0_distance = shortest_distance
        shortest_distance = float("inf")
        # print(f"point: {point} distance: {self.get_distances_to_point_on_wire(1, point)}")
        for distance in self.get_distances_to_point_on_wire(1, point):
            # print(f"distance: {distance}")
            if distance < shortest_distance:
                shortest_distance = distance
        wire_1_distance = shortest_distance
        return wire_0_distance + wire_1_distance
        

def get_new_pos(position, move):
    """
    Arguments:
        position(int, int): (12, 14)
        move(str): R1001
    """
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
    shortest_distance = float("inf")
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
    line_0_points = starmap.get_points(0, wires_segments[0])
    # print(f"line_0_points: {line_0_points}")
    # print(f"starmap.wires_distance_to_points[0]: {starmap.wires_distance_to_points[0]}")
    line_1_points = starmap.get_points(1, wires_segments[1])
    intersections = find_intersections(line_0_points, line_1_points)
    # print(f"intersections: {intersections}")

    if intersections:
        shortest_total_distance = float("inf")
        shortest_distance = find_shortest_distance(intersections)
        # print(f"shortest_distance: {shortest_distance}")
        for point in intersections:
            total_distance = starmap.get_shortest_total_distance_to_point(point)
            if total_distance < shortest_total_distance:
                shortest_total_distance = total_distance
        print(shortest_total_distance)

main()
