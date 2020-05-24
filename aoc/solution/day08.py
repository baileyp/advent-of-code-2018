from collections import deque


def part1(file):
    """
    O(n + e) time and and O(n) space, where e is the number of edges (parent-child relationship) defined by the input
    :param file:
    :return:
    """
    return build_graph(file).meta_value()


def part2(file):
    """
    O(n + e) time and and O(n) space, where e is the number of edges (parent-child relationship) defined by the input
    :param file:
    :return:
    """
    return build_graph(file).value()


def build_graph(file):
    license_file = deque(int(n) for n in file.single_line().split(' '))
    return parse_license(license_file, Node())


def parse_license(remainder, node):
    # Pull the header from the remainder of the license
    header = remainder.popleft(), remainder.popleft()

    # For each child specified in the header, parse the license remainder
    for _ in range(header[0]):
        child = parse_license(remainder, Node())
        node.add_child(child)

    # Since all the children have been processed, this node's metadata is now at the head of the remainder
    for _ in range(header[1]):
        node.add_meta(remainder.popleft())

    # Freshly built node, children and all
    return node


class Node:
    def __init__(self):
        self._meta = list()
        self._children = list()

    def add_meta(self, meta):
        self._meta.append(meta)

    def add_child(self, node):
        self._children.append(node)

    def meta_value(self):
        # Recursively sum the metadata values
        return sum(self._meta) + sum(child.meta_value() for child in self._children)

    def value(self):
        num_children = len(self._children)
        # Just the metadata value
        if num_children == 0:
            return self.meta_value()
        # Recursively sum the child values, indexed by the metadata
        return sum(self._children[i - 1].value() for i in self._meta if i <= num_children)
