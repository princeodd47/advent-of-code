import pytest
from unittest import mock

from aoc2015 import day_06


@pytest.mark.parametrize(
    ("input_string", "expected_result"),
    [
        (["turn on 0,0 through 999,999"],
            [
                {
                    'action': 'turn on',
                    'begin_x': 0,
                    'begin_y': 0,
                    'end_x': 999,
                    'end_y': 999
                }
            ]
        ),
        (["toggle 0,0 through 999,0"],
            [
                {
                    'action': 'toggle',
                    'begin_x': 0,
                    'begin_y': 0,
                    'end_x': 999,
                    'end_y': 0
                }
            ]
        ),
        (["turn off 499,499 through 500,500"],
            [
                {
                    'action': 'turn off',
                    'begin_x': 499,
                    'begin_y': 499,
                    'end_x': 500,
                    'end_y':500 
                }
            ]
        ),
    ]
)
def test__sanitize_input(input_string, expected_result):
    return_value = day_06._sanitize_input(input_string)
    assert return_value == expected_result
