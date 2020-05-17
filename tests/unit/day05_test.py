import pytest

from aoc.solution import day05


@pytest.mark.parametrize('polymer, expected', [
    ('dabAcCaCBAcCcaDA', 'dabCBAcaDA'),
    ('abcCdeeF', 'abdeeF'),
])
def test_react(polymer, expected):
    assert day05.react(polymer) == expected
