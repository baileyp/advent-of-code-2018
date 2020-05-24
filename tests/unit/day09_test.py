from unittest import mock
from aoc.solution import day09
from aoc.util import FileReader


def test_parse_input():
    mock_file_reader = mock.MagicMock(spec=FileReader)
    mock_file_reader.single_line.return_value = '10 players; last marble is worth 1618 points'
    assert day09.parse_input(mock_file_reader) == (10, 1618)
