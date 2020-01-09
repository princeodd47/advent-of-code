from aoc2019 import day_04


def test_part1():
    result = day_04.get_good_num_count(130254, 678275)
    assert result == 2090


def test_part2():
    result = day_04.get_good_num_count_p2(130254, 678275)
    assert result == 1419
