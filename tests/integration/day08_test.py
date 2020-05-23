import pytest
from io import StringIO

from aoc.solution import day08
from aoc.util import FileReader


@pytest.mark.parametrize('test_case, result', [
    ("2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2", 138),
    ("2 3 1 3 0 1 99 10 11 12 0 1 2 1 1 2", 138),
])
def test_part_1(test_case, result):
    file = StringIO(test_case)
    assert day08.part1(FileReader(file)) == result


@pytest.mark.parametrize('test_case, result', [
    ("2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2", 66),
])
def test_part_2(test_case, result):
    file = StringIO(test_case)
    assert day08.part2(FileReader(file)) == result
