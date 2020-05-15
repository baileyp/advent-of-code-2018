import pytest
from io import StringIO

from aoc.solution import day02
from aoc.util import FileReader


@pytest.mark.parametrize('test_case, result', [
    ('abcdef, bababc, abbcde, abcccd, aabcdd, abcdee, ababab', 12),
])
def test_part_1(test_case, result):
    file = StringIO(test_case.replace(', ', "\n"))
    assert day02.part1(FileReader(file)) == result

@pytest.mark.parametrize('test_case, result', [
    ('abcde, fghij, klmno, pqrst, fguij, axcye, wvxyz', 'fgij')
])
def test_part_2(test_case, result):
    file = StringIO(test_case.replace(', ', "\n"))
    assert day02.part2(FileReader(file)) == result