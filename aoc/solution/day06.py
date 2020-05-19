from collections import defaultdict, Counter


def part1(file):
    """
    O(n * x * y) time and O(n) space, where x and y are the width and height of the grid defined by the coordinates
    :param file:
    :return:
    """
    points = [tuple(map(int, line.split(', '))) for line in file]
    infinite_regions = set()
    regions = defaultdict(lambda: 0)
    left_bound = min(p[0] for p in points)
    right_bound = max(p[0] for p in points)
    top_bound = min(p[1] for p in points)
    bottom_bound = max(p[1] for p in points)

    for x in range(left_bound, right_bound + 1):
        for y in range(top_bound, bottom_bound + 1):
            # Build a map of distance => points at that distances
            distances = defaultdict(lambda: set())
            for p in points:
                distances[manhattan_distance(p, (x, y))].add(p)

            # Find then closest point(s) and if there is only one closest, increment it's area
            closest = distances[min(distances.keys())]
            if len(closest) == 1:
                closest = closest.pop()
                regions[closest] += 1

                # Any region point that is on the grid boundary is infinite, so keep track of its closest point
                if x in (left_bound, right_bound) or y in (top_bound, bottom_bound):
                    infinite_regions.add(closest)

    # Remove all defined regions that are also infinite
    for area in infinite_regions:
        regions.pop(area)

    return max(regions.values())


def part2(file, max_sum=10000):
    """
    O(n * x * y) time and O(n) space, where x and y are the width and height of the grid defined by the coordinates
    :param file:
    :param max_sum:
    :return:
    """
    points = [tuple(map(int, line.split(', '))) for line in file]
    left_bound = min(p[0] for p in points)
    right_bound = max(p[0] for p in points)
    top_bound = min(p[1] for p in points)
    bottom_bound = max(p[1] for p in points)
    region_size = 0

    # For every location within the boundary, sum its distance to every point. If less than the max, its part of the
    # target region
    for x in range(left_bound, right_bound + 1):
        for y in range(top_bound, bottom_bound + 1):
            foo = sum(manhattan_distance(p, (x, y)) for p in points)
            if foo < max_sum:
                region_size += 1

    return region_size


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
