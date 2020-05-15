import pytest

from aoc.solution import day03


@pytest.mark.parametrize('pattern, matches', [
    ('#123 @ 3,2: 5x4', (123, 3, 2, 5, 4)),
    ('#456 @ 31,72: 25x40', (456, 31, 72, 25, 40)),
    ('#1 @ 0,0: 2x2', (1, 0, 0, 2, 2)),
])
def test_parse_claim(pattern, matches):
    assert day03.parse_claim(pattern) == matches


@pytest.mark.parametrize('claim', [
    '#123@3,2:5x4',
    '#123 @ 3,2: 5 x 4',
    '#123  3,2: 5x4',
    '',
])
def test_parse_claim_invalid_claim_raises_exception(claim):
    with pytest.raises(ValueError):
        day03.parse_claim(claim)

@pytest.mark.parametrize('initial, row, expected', [
    (0, {1: 1, 2: 2, 3: 3, 4: 1}, 2),
    (8, {1: 1, 2: 2, 3: 3, 4: 1}, 10),
    (0, {1: 3, 2: 2, 3: 3, 4: 1}, 3),
    (0, {1: 1, 2: 1, 3: 1, 4: 1}, 0),
])
def test_reducer(initial, row, expected):
    assert day03.reducer(initial, row) == expected
