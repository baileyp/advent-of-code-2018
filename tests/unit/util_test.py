import pytest

from aoc.util import FileReader


class TestFileReader:

    def test_iteration(self):
        reader = FileReader(['No Whitespace', '\tWith Whitespace   '])
        assert list(reader) == ['No Whitespace', 'With Whitespace']

    @pytest.mark.parametrize('lines, break_after, expected', [
        (['First', 'Second'], 3, 2),
        (['First', 'Second', 'Third', 'Fourth'], 3, 1),
        (['First', 'Second', 'Third', 'Fourth'], 15, 4),
    ])
    def test_iter_circular(self, lines, break_after, expected):
        reader = FileReader(lines)
        seen = list([])
        counter = 0

        for line in reader.iter_circular():
            if counter == break_after:
                break
            seen.append(line)
            counter += 1

        assert seen.count(lines[0]) == expected
