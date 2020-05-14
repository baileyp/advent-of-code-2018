import pytest
from io import StringIO

from aoc.solution import day01
from aoc.util import FileReader


@pytest.mark.parametrize('test_case, result', [
    ('+1, -2, +3, +1', 3),
    ('+1, +1, +1', 3),
    ('+1, +1, -2', 0),
    ('-1, -2, -3', -6),
])
def test_part_1(test_case, result):
    file = StringIO(test_case.replace(', ', "\n"))
    assert day01.part1(FileReader(file)) == result

@pytest.mark.parametrize('test_case, result', [
    ('+1, -2, +3, +1, +1, -2', 2),
    ('1, -1', 0),
    ('+3, +3, +4, -2, -4', 10),
    ('-6, +3, +8, +5, -6', 5),
    ('+7, +7, -2, -7, -4', 14),
])
def test_part_2(test_case, result):
    file = StringIO(test_case.replace(', ', "\n"))
    assert day01.part2(FileReader(file)) == result
