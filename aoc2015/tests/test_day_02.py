import pytest

from aoc2015 import day_02


@pytest.mark.parametrize(
    ("input_string", "expected_result"),
    [
        ("2x3x4", 58),
        ("1x1x10", 43),
    ]
)
def test_part1(input_string, expected_result):
    return_value = day_02._calculate_amount(input_string)
    assert return_value == expected_result


@pytest.mark.parametrize(
    ("input_values", "expected_result"),
    [
        ([2,3,4], 10),
        ([1,1,10], 4),
    ]
)
def test_calculate_ribbon_for_present(input_values, expected_result):
    return_value = day_02._calculate_ribbon_for_present(input_values)
    assert return_value == expected_result


@pytest.mark.parametrize(
    ("input_values", "expected_result"),
    [
        ([2,3,4], 24),
        ([1,1,10], 10),
    ]
)
def test_calculate_ribbon_for_bow(input_values, expected_result):
    return_value = day_02._calculate_ribbon_for_bow(input_values)
    assert return_value == expected_result


@pytest.mark.parametrize(
    ("input_string", "expected_result"),
    [
        ("2x3x4", 34),
        ("1x1x10", 14),
    ]
)
def test_part2(input_string, expected_result):
    return_value = day_02._calculate_ribbon(input_string)
    assert return_value == expected_result
