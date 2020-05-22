import pytest
from unittest import mock
from aoc.solution import day07


@pytest.mark.parametrize('node, graph, expected', [
    ('a', {'one': [1, 2, 3], 'two': ['c', 'a', 'b']}, False),
    ('d', {'one': [1, 2, 3], 'two': ['c', 'a', 'b']}, True),
    (1, {'one': [1, 2, 3], 'two': ['c', 'a', 'b']}, False),
    ('1', {'one': [1, 2, 3], 'two': ['c', 'a', 'b']}, True),
])
def test_is_available(node, graph, expected):
    assert day07.is_available(node, graph) == expected


def test_instruction_duration():
    assert day07.instruction_duration('A') == 1
    assert day07.instruction_duration('Z') == 26


class TestTimedInstruction:
    def test_hooks(self):
        ti_A5 = day07.TimedInstruction('A', 5)
        ti_A3 = day07.TimedInstruction('A', 3)
        ti_B3 = day07.TimedInstruction('B', 3)

        # __eq__
        assert ti_A5 == ti_A3
        assert ti_A3 != ti_B3

        # __lt__ and __gt__
        assert ti_A5 < ti_B3
        assert ti_B3 > ti_A3

        # __hash__
        assert hash(ti_A5) == 65
        assert hash(ti_B3) == 66

    @pytest.mark.parametrize('instruction, base, duration, expected', [
        ('A', 0, 3, 3),
        ('A', 60, 3, 63),
    ])
    def test_from_instruction(self, instruction, base, duration, expected):
        with mock.patch.object(day07, 'instruction_duration') as mock_instruction_duration:
            mock_instruction_duration.return_value = duration
            ti = day07.TimedInstruction.from_instruction(instruction, base)
            assert ti.instruction == instruction
            assert ti.duration == expected

    @pytest.mark.parametrize('duration, ticks, expected', [
        (3, 1, 2),
        (3, 3, 0),
        (3, 4, -1),
    ])
    def test_tick(self, duration, ticks, expected):
        ti = day07.TimedInstruction('A', duration)
        for _ in range(ticks):
            ti.tick()

        assert ti.duration == expected

    @pytest.mark.parametrize('duration, expected', [
        (1, False),
    ])
    def test_done(self, duration, expected):
        ti = day07.TimedInstruction('A', duration)
        assert ti.done() is expected


class TestWorkerPool:
    def test_elapsed(self):
        wp = day07.WorkerPool(1)
        assert wp.elapsed() == 0

    def test_assign_is_assignable(self):
        wp = day07.WorkerPool(2)

        assert wp.is_assignable('A')
        assert wp.is_assignable('B')
        assert wp.is_assignable('C')

        wp.assign('A')
        assert not wp.is_assignable('A')
        assert wp.is_assignable('B')
        assert wp.is_assignable('C')

        wp.assign('C')
        assert not wp.is_assignable('A')
        assert wp.is_assignable('B')
        assert not wp.is_assignable('C')

        wp.assign('B')
        assert not wp.is_assignable('A')
        assert wp.is_assignable('B')
        assert not wp.is_assignable('C')

    def test_tick(self):
        wp = day07.WorkerPool(2)

        mock_ti1 = mock.MagicMock(spec=day07.TimedInstruction)
        mock_ti2 = mock.MagicMock(spec=day07.TimedInstruction)
        mock_ti1.done.side_effect = [False, True]
        mock_ti2.done.return_value = False

        wp.assign(mock_ti1)
        wp.assign(mock_ti2)

        completed = wp.tick()

        assert mock_ti1.tick.call_count == 2
        assert mock_ti1.done.call_count == 2
        assert mock_ti2.tick.call_count == 2
        assert mock_ti2.done.call_count == 2

        assert len(completed) == 1
        assert completed.pop() == mock_ti1
