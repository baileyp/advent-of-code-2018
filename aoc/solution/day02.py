from collections import defaultdict
from functools import reduce
from operator import mul

from aoc.exceptions import DesignError


def part1(file):
    """
    O(n * l) time and O(l) space, where l is the length of the IDs.
    :param file:
    :return:
    """
    # Character counts to track
    contains = {2: 0, 3: 0}
    for line in file:
        # Build a map of letter => occurrences
        counts = defaultdict(lambda: 0)
        for char in line:
            counts[char] += 1

        # Count up how many occurrences
        counts = counts.values()
        for key in contains.keys():
            if key in counts:
                contains[key] += 1

    # Reduce counts as product
    return reduce(mul, contains.values(), 1)


def part2(file):
    """
    O(n) time and O(n * l) space, where l is the length of the IDs.
    :param file:
    :return:
    """
    # This will store "hashes" of IDs
    seen = set()
    for line in file:
        for i in range(len(line)):
            # Hashes are just a wildcard char in place of every actual char
            hashed = ''.join([line[:i], '*', line[i + 1:]])
            if hashed in seen:
                return hashed.replace('*', '')
            seen.add(hashed)

    # This code should not be reachable
    raise DesignError
