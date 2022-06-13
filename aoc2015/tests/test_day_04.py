import pytest
from unittest import mock

from aoc2015 import day_04


@pytest.mark.parametrize(
    ("input_string", "expected_result"),
    [
        ("abcdef", 609043),
        ("pqrstuv", 1048970),
    ]
)
def test_part1(input_string, expected_result):
    return_value = day_04._find_hash(input_string, 5)
    assert return_value == expected_result
