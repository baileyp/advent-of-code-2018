import pytest

from aoc.solution import day06


@pytest.mark.parametrize('p1, p2, expected', [
    ((0, 0), (0, 1), 1),
    ((0, 0), (1, 1), 2),
    ((-9, 13), (-5, -4), 21),
])
def test_manhattan_distance(p1, p2, expected):
    assert day06.manhattan_distance(p1, p2) == expected
