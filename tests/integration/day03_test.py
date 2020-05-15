import pytest
from io import StringIO

from aoc.solution import day03
from aoc.util import FileReader


@pytest.mark.parametrize('test_case, result', [
    ('#1 @ 1,3: 4x4; #2 @ 3,1: 4x4; #3 @ 5,5: 2x2', 4),
    ('#123 @ 3,2: 5x4', 0),
])
def test_part_1(test_case, result):
    file = StringIO(test_case.replace('; ', "\n"))
    assert day03.part1(FileReader(file)) == result


@pytest.mark.parametrize('test_case, result', [
    ('#1 @ 1,3: 4x4; #2 @ 3,1: 4x4; #3 @ 5,5: 2x2', 3),
    ('#123 @ 3,2: 5x4', 123),
])
def test_part_2(test_case, result):
    file = StringIO(test_case.replace('; ', "\n"))
    assert day03.part2(FileReader(file)) == result
