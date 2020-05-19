import pytest
from io import StringIO

from aoc.solution import day06
from aoc.util import FileReader


@pytest.mark.parametrize('test_case, result', [
    ("1, 1; 1, 6; 8, 3; 3, 4; 5, 5; 8, 9", 17),
])
def test_part_1(test_case, result):
    file = StringIO(test_case.replace('; ', "\n"))
    assert day06.part1(FileReader(file)) == result

@pytest.mark.parametrize('test_case, result', [
    ("1, 1; 1, 6; 8, 3; 3, 4; 5, 5; 8, 9", 16),
])
def test_part_2(test_case, result):
    file = StringIO(test_case.replace('; ', "\n"))
    assert day06.part2(FileReader(file), 32) == result
