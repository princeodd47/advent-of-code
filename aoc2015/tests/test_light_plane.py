import pytest
from unittest import mock

from aoc2015 import light_plane


@pytest.mark.parametrize(
    ("input_max_x", "input_max_y", "expected_total_points"),
    [
        (5, 5, 25),
        (2, 5, 10),
        (1000, 1000, 1000000),
    ]
)
def test_plane(input_max_x, input_max_y, expected_total_points):
    plane = light_plane.Plane(input_max_x, input_max_y)
    assert plane.total_points == expected_total_points
    assert plane.total_points_off == expected_total_points
    assert plane.total_points_on == 0


@pytest.mark.parametrize(
    ("input_actions", "input_max_x", "input_max_y", "expected_on", "expected_off"),
    [
        (
            [
                {
                    'action': 'turn on',
                    'begin_x': 0,
                    'begin_y': 0,
                    'end_x': 999,
                    'end_y': 999
                },
                {
                    'action': 'toggle',
                    'begin_x': 0,
                    'begin_y': 0,
                    'end_x': 999,
                    'end_y': 0
                },
                {
                    'action': 'turn off',
                    'begin_x': 499,
                    'begin_y': 499,
                    'end_x': 500,
                    'end_y':500 
                },
            ],
            1000,
            1000,
            998996,
            1004
        ),
    ]
)
def test_commit_actions(input_actions, input_max_x, input_max_y, expected_on, expected_off):
    plane = light_plane.Plane(input_max_x, input_max_y)
    plane.commit_actions(input_actions)
    assert plane.total_points_on == expected_on
    assert plane.total_points_off == expected_off


@pytest.mark.parametrize(
    ("input_actions", "input_max_x", "input_max_y", "expected_brightness", "expected_on", "expected_off"),
    [
        (
            [
                {
                    'action': 'toggle',
                    'begin_x': 0,
                    'begin_y': 0,
                    'end_x': 999,
                    'end_y': 999
                },
            ],
            1000,
            1000,
            2000000,
            1000000,
            0
        ),
    ]
)
def test_commit_actions_part2(input_actions, input_max_x, input_max_y, expected_brightness, expected_on, expected_off):
    plane = light_plane.Plane(input_max_x, input_max_y)
    plane.commit_actions_part2(input_actions)
    assert plane.total_brightness == expected_brightness
    assert plane.total_points_on == expected_on
    assert plane.total_points_off == expected_off
