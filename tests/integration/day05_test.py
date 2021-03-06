import pytest
from io import StringIO

from aoc.solution import day05
from aoc.util import FileReader


@pytest.mark.parametrize('test_case, result', [
    ("dabAcCaCBAcCcaDA", 10)
])
def test_part_1(test_case, result):
    file = StringIO(test_case)
    assert day05.part1(FileReader(file)) == result

@pytest.mark.parametrize('test_case, result', [
    ("dabAcCaCBAcCcaDA", 4)
])
def test_part_2(test_case, result):
    file = StringIO(test_case)
    assert day05.part2(FileReader(file)) == result
