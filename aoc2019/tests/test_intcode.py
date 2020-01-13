from aoc2019.intcode import IntCode

def test_halt_and_restart():
    intcode = IntCode()
    intcode.get_input("input/day_07")
    intcode.set_user_input([1, 2])
    intcode.diagnostic_program()
    return_value = intcode.result

    intcode = IntCode()
    intcode.get_input("input/day_07")
    intcode.set_user_input([1])
    intcode.diagnostic_program()
    intcode.set_user_input([2])
    intcode.diagnostic_program()
    assert return_value == intcode.result
