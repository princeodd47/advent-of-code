from . import cartesian_plane
from . import common


def part1():
    print(get_number_of_houses_visited())

def get_number_of_houses_visited():
    plane = cartesian_plane.Plane()
    instructions = common.get_input_as_single_string("input/day_03")
    for i in instructions:
        if i == "^":
            plane.move_up()
        elif i == ">":
            plane.move_right()
        elif i == "v":
            plane.move_down()
        elif i == "<":
            plane.move_left()
    return plane.number_of_points


def part2():
    print(get_number_of_houses_visited_with_robo())


def get_number_of_houses_visited_with_robo():
    who = "santa"
    counter = 0
    plane = cartesian_plane.Plane(robo=True)
    instructions = common.get_input_as_single_string("input/day_03")
    for i in instructions:
        if (counter % 2) == 0:
            who = "santa"
        else:
            who = "robo"
        if i == "^":
            plane.move_up(who)
        elif i == ">":
            plane.move_right(who)
        elif i == "v":
            plane.move_down(who)
        elif i == "<":
            plane.move_left(who)
        counter += 1
    return plane.number_of_points
