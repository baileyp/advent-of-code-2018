import pytest
from unittest import mock
from aoc.solution import day08


class TestNode:
    def test_add_meta(self):
        node = day08.Node()
        with mock.patch.object(node, '_meta') as mock_meta:
            node.add_meta('meta')
            assert mock_meta.append.called_once_with('meta')

    def test_add_child(self):
        node = day08.Node()
        with mock.patch.object(node, '_children') as mock_children:
            node.add_child('child')
            assert mock_children.append.called_once_with('child')

    def test_meta_value(self):
        node = day08.Node()
        assert node.meta_value() == 0

        node.add_meta(4)
        node.add_meta(3)
        assert node.meta_value() == 7

        child = day08.Node()
        child.add_meta(5)
        child.add_meta(5)
        assert child.meta_value() == 10

        node.add_child(child)
        assert node.meta_value() == 17

    def test_value(self):
        node = day08.Node()
        assert node.value() == 0

        node.add_meta(3)
        assert node.value() == 3

        child = day08.Node()
        child.add_meta(5)
        node.add_child(child)
        assert node.value() == 0

        node.add_meta(1)
        assert node.value() == 5
