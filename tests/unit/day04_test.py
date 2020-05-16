import pytest
from datetime import datetime

from aoc.solution import day04


@pytest.mark.parametrize('pattern, matches', [
    ('[1518-07-18 23:57] Guard #157 begins shift', (157, day04.SHIFT, datetime(1518, 7, 18, 23, 57))),
    ('[1518-04-18 00:44] wakes up', (None, day04.WAKE, datetime(1518, 4, 18, 0, 44))),
    ('[1518-10-26 00:20] falls asleep', (None, day04.SLEEPS, datetime(1518, 10, 26, 0, 20))),
])
def test_parse_note(pattern, matches):
    assert day04.parse_note(pattern) == matches


@pytest.mark.parametrize('claim', [
    '[1518-07-18 23:57]Guard #157 begins shift',
    '',
])
def test_parse_note_invalid_note_raises_exception(claim):
    with pytest.raises(ValueError):
        day04.parse_note(claim)
