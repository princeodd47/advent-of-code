from . import common
from . import coordinates
from . import submarine


def part1():
    print(find_values_p1("input/day_02"))
    # answer: 1694130

def part2():
    print(find_values_p2("input/day_02"))
    # answer: 1698850445


def find_values_p1(input_file):
    values = common.get_input_as_strings(input_file)
    movement = _parse_input(values)
    # print(f'{movement=}')
    position = coordinates.Coordinates(x=0, y=0)
    # print(f'{position.x=} {position.y=}')
    _follow_instructions(position, movement)
    print(f'{position.x=} {position.y=}')
    return abs(position.x * position.y)


def _parse_input(input_values):
    movement = []
    for value in input_values:
        value_split = value.split(' ')
        movement.append({'direction': value_split[0], 'value':  int(value_split[1])})
    return movement


def _follow_instructions(position, movement):
    for move in movement:
        # print(f'{move=}')
        if move['direction'] == 'forward':
            position.move_right(move['value'])
        elif move['direction'] == 'down':
            position.move_down(move['value'])
        elif move['direction'] == 'up':
            position.move_up(move['value'])
        # print(f'{position.x=} {position.y=}')
        

def find_values_p2(input_file):
    values = common.get_input_as_strings(input_file)
    movement = _parse_input(values)
    position = submarine.Submarine(x=0, y=0, aim=0)
    _follow_submarine_instructions(position, movement)
    print(f'{position.x=} {position.y=}')
    return abs(position.x * position.y)


def _follow_submarine_instructions(position, movement):
    for move in movement:
        # print(f'{move=}')
        if move['direction'] == 'forward':
            position.move_forward(move['value'])
        elif move['direction'] == 'down':
            position.increase_aim(move['value'])
        elif move['direction'] == 'up':
            position.decrease_aim(move['value'])
        # print(f'{position.x=} {position.y=}')
