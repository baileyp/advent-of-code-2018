import pytest
from io import StringIO

from aoc.solution import day07
from aoc.util import FileReader


@pytest.mark.parametrize('test_case, result', [
    ("""Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.""", 'CABDFE'),
    ("""Step C must be finished before step A can begin.
Step E must be finished before step A can begin.
Step C must be finished before step B can begin.
Step A must be finished before step D can begin.
Step G must be finished before step D can begin.
Step B must be finished before step F can begin.
Step A must be finished before step F can begin.
Step D must be finished before step F can begin.
Step E must be finished before step G can begin.""", 'CBEAGDF')
])
def test_part_1(test_case, result):
    file = StringIO(test_case)
    assert day07.part1(FileReader(file)) == result

@pytest.mark.parametrize('test_case, result', [
    ("""Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.""", 15)
])
def test_part_2(test_case, result):
    file = StringIO(test_case)
    assert day07.part2(FileReader(file), 0, 2) == result
