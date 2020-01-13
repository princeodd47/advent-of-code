from .intcode import IntCode


def part1():
    intcode = IntCode()
    intcode.get_input("input/day_02")
    intcode.set_user_input(None)
    value = intcode.diagnostic_program()
    print(value)
