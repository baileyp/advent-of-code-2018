from unittest import mock

import pytest

from aoc.solution import day11

@pytest.mark.parametrize('x, y, sn, expected', [
    (3, 5, 8, 4),
    (122, 79, 57, -5),
    (217, 196, 39, 0),
    (101, 153, 71, 4),
])
def test_power_level(x, y, sn, expected):
    assert day11.power_level(x, y, sn) == expected


@pytest.mark.parametrize('x, y, size, expected', [
    (1, 2, 2, [(1, 2), (1, 3), (2, 2), (2, 3)]),
])
def test_square(x, y, size, expected):
    points = day11.square(x, y, size)
    assert list(points) == expected
