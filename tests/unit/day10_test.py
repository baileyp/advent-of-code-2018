from unittest import mock
from aoc.solution import day10


def make_mock_point(x, y):
    mock_point = mock.MagicMock(spec=day10.Point)
    mock_point.x.return_value = x
    mock_point.y.return_value = y
    return mock_point


def test_move():
    mock_point = mock.MagicMock(spec=day10.Point)
    assert day10.move([mock_point]) == 1
    mock_point.move.assert_called_once()


def test_size():
    p1 = make_mock_point(-1, 5)
    p2 = make_mock_point(6, 3)
    p3 = make_mock_point(4, -2)

    assert day10.size([p1, p2, p3]) == (-1, 6, -2, 5)


def test_points():
    with mock.patch.object(day10, 'Point') as mock_point:
        file = ['1 blah 2 blah 4 blah 10']
        for _ in day10.points(file):
            mock_point.assert_called_once_with((1, 2), (4, 10))

    with mock.patch.object(day10, 'Point') as mock_point:
        file = ['1 blah -2 blah 4 blah -10']
        for _ in day10.points(file):
            mock_point.assert_called_once_with((1, -2), (4, -10))


class TestPoint:
    def test_x_y(self):
        point = day10.Point((1, 2), (4, -3))
        assert point.x() == 1
        assert point.y() == 2

    def test_move(self):
        point = day10.Point((1, 2), (4, -3))
        point.move()
        assert point.x() == 5
        assert point.y() == -1

    def test_equality(self):
        point = day10.Point((1, 2), (4, -3))
        assert point == (1, 2)
        assert point != (2, 1)
