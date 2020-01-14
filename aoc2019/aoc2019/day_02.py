from .intcode import IntCode


def part1():
    intcode = IntCode()
    intcode.get_input("input/day_02")
    value = intcode.diagnostic_program()
    print(value)
