import pytest

from aoc.util import FileReader


class TestFileReader:

    @pytest.mark.parametrize('lines, break_after, expected', [
        (['First', 'Second'], 3, 2),
        (['First', 'Second', 'Third', 'Fourth'], 3, 1),
        (['First', 'Second', 'Third', 'Fourth'], 15, 4),
    ])
    def test_iter_infinite(self, lines, break_after, expected):
        reader = FileReader(lines)
        seen = list([])
        counter = 0

        for line in reader.iter_infinite():
            if counter == break_after:
                break
            seen.append(line)
            counter += 1

        assert seen.count(lines[0]) == expected
