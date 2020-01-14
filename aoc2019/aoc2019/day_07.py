from itertools import permutations

from aoc2019.intcode import IntCode


def part1():
    # input_file = "input/day_07"
    # phase_seq = "43210"
    # input_file = "input/day_07_p1_ex1"

    # phase_seq = "01234"
    # input_file = "input/day_07_p1_ex2"

    # phase_seq = "10432"
    # input_file = "input/day_07_p1_ex3"
    results = []

    perm = permutations([0, 1, 2, 3, 4])
    for p in perm:
        phase_seq = str(p[0]) + str(p[1]) + str(p[2]) + str(p[3]) + str(p[4])
        input_file = "input/day_07"

        amp_a = IntCode()
        amp_a.get_input(input_file)
        amp_a.set_user_input([phase_seq[0], 0])
        amp_a.diagnostic_program()
        result_a = amp_a.result

        amp_b = IntCode()
        amp_b.get_input(input_file)
        amp_b.set_user_input([phase_seq[1], result_a])
        amp_b.diagnostic_program()
        result_b = amp_b.result

        amp_c = IntCode()
        amp_c.get_input(input_file)
        amp_c.set_user_input([phase_seq[2], result_b])
        amp_c.diagnostic_program()
        result_c = amp_c.result

        amp_d = IntCode()
        amp_d.get_input(input_file)
        amp_d.set_user_input([phase_seq[3], result_c])
        amp_d.diagnostic_program()
        result_d = amp_d.result

        amp_e = IntCode()
        amp_e.get_input(input_file)
        amp_e.set_user_input([phase_seq[4], result_d])
        amp_e.diagnostic_program()
        result_e = amp_e.result

        # print(result_e)
        results.append(result_e)

    print(max(results))


def part2():
    pass
