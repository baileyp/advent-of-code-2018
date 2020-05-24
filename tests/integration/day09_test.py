import pytest
from io import StringIO

from aoc.solution import day09
from aoc.util import FileReader


@pytest.mark.parametrize('test_case, result', [
    ('7 players; last marble is worth 25 points', 32),
    ('10 players; last marble is worth 1618 points', 8317),
    ('13 players; last marble is worth 7999 points', 146373),
    ('17 players; last marble is worth 1104 points', 2764),
    ('21 players; last marble is worth 6111 points', 54718),
    ('30 players; last marble is worth 5807 points', 37305),
])
def test_part_1(test_case, result):
    file = StringIO(test_case)
    assert day09.part1(FileReader(file)) == result
