import pytest
from io import StringIO

from aoc.solution import day11
from aoc.util import FileReader


@pytest.mark.parametrize('test_case, result', [
    ('18', '33,45'),
    ('42', '21,61'),
])
def test_part_1(test_case, result):
    file = StringIO(test_case)
    assert day11.part1(FileReader(file)) == result

@pytest.mark.parametrize('test_case, result', [
    ('18', '90,269,16'),
    ('42', '232,251,12'),
])
def test_part_2(test_case, result):
    file = StringIO(test_case)
    assert day11.part2(FileReader(file)) == result