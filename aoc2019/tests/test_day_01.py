import pytest

from aoc2019 import day_01


def test_part1():
    return_value = day_01.part1()
    assert return_value == 3366415


def test_part2():
    return_value = day_01.part2()
    assert return_value == 5046772
