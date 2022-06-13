import pytest
from unittest import mock

from aoc2015 import day_05


@pytest.mark.parametrize(
    ("input_string", "expected_result"),
    [
        ("ugknbfddgicrmopn", "nice"),
        ("aaa", "nice"),
        ("jchzalrnumimnmhp", "naughty"),
        ("haegwjzuvuyypxyu", "naughty"),
        ("dvszwmarrgswjxmb", "naughty"),
    ]
)
def test__get_classification_part1(input_string, expected_result):
    return_value = day_05._get_classification_part1(input_string)
    assert return_value == expected_result


@pytest.mark.parametrize(
    ("input_string", "expected_result"),
    [
        ("qjhvhtzxzqqjkmpb", "nice"),
        ("xxyxx", "nice"),
        ("uurcxstgmygtbstg", "naughty"),
        ("ieodomkazucvgmuy", "naughty"),
        ("opmopgyabjjjoygt", "nice"),
        ("sknufchjdvccccta", "nice"),
        ("cyypypveppxxxfuq", "nice"),
        ("aaaa", "nice"),
        ("xyxy", "nice"),
        ("abaaaa", "nice"),
    ]
)
def test__get_classification_part2(input_string, expected_result):
    return_value = day_05._get_classification_part2(input_string)
    assert return_value == expected_result
