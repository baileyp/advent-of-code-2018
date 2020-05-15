from builtins import sum

from aoc.exceptions import DesignError


def part1(file):
    """
    O(n) space and time
    :param file:
    :return:
    """
    # Trivial, just sum up all the inputs
    return sum(int(line) for line in file)


def part2(file):
    """
    O(n) space and time
    :param file:
    :return:
    """
    frequency = 0
    found = {frequency}

    # Loop continuously over inputs
    for line in file.iter_circular():
        frequency += int(line)
        if frequency in found:
            # 2nd time frequency encountered, this is the answer
            return frequency
        # Track the new frequency
        found.add(frequency)

    # This code should not be reachable
    raise DesignError
