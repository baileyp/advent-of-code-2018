import re
from collections import defaultdict
from functools import reduce

from aoc.exceptions import DesignError


def part1(file):
    """
    O(n * w * h) time complexity, and O(w * h) space complexity, where w and h are the aggregate width and height of
    all claims
    :param file:
    :return:
    """
    grid = defaultdict(lambda: defaultdict(lambda: 0))
    for claim in file:
        claim_id, left, top, width, height = parse_claim(claim)
        for col in range(width):
            for row in range(height):
                # All grid points will contain an integer representing the number of claims for that square inch
                grid[left + col][top + row] += 1

    return reduce(reducer, grid.values(), 0)


def part2(file):
    """
    O(n * w * h) time and space complexity, where w and h are the aggregate width and height of all claims
    :param file:
    :return:
    """
    grid = defaultdict(lambda: defaultdict(lambda: set()))
    claims = set()
    for claim in file:
        claim_id, left, top, width, height = parse_claim(claim)
        claims.add(claim_id)
        for col in range(width):
            for row in range(height):
                # Push each claim ID onto the square
                grid[left + col][top + row].add(claim_id)

    for row in grid.values():
        for claims_at_square in row.values():
            if len(claims_at_square) > 1:
                # For every square with more than one claim, subtract those claim IDs from all known claim IDs
                claims -= claims_at_square

    # Per the problem statement, only one claim ID remains
    return claims.pop()


def parse_claim(claim):
    pattern = re.compile(r"^\#(\d+) \@ (\d+),(\d+): (\d+)x(\d+)$")
    if re.match(pattern, claim):
        return tuple(int(match) for match in re.findall(pattern, claim).pop())
    raise ValueError("Invalid claim format")


def reducer(carry, row):
    # Return a sum of how square inches have more than one claim, plus the carry
    return carry + sum(1 for s in row.values() if s > 1)
