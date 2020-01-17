from .intcode import IntCode


def part1():
    boost = IntCode()
    boost.get_input("input/day_09")
    boost.set_user_input([1])
    boost.diagnostic_program()
    print(f"{boost.result_history=}")



def part2():
    pass
