import pytest

from aoc2019.intcode import IntCode


def test_d5p1():
    intcode = IntCode()
    intcode.get_input("input/day_05")
    intcode.diagnostic_program(1)
    assert intcode.result == 16489636

def test_d5_examples():
    intcode = IntCode()
    intcode.data = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
    intcode.diagnostic_program(0)
    assert intcode.result == 0

def test_d5p2():
    intcode = IntCode()
    intcode.get_input("input/day_05")
    intcode.diagnostic_program(5)
    assert intcode.result == 9386583
