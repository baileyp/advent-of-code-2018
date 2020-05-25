import re
from contextlib import redirect_stdout
from io import StringIO


def part1(file, run_interactive=True, num_moves=0):
    """
    O(n) space and O(n * t) time where t is the number of seconds before the message appears
    :param file:
    :param run_interactive:
    :param num_moves:
    :return:
    """
    sky = list(points(file))
    elapsed = 0

    if run_interactive:
        # First, move all the points until they coalesce a grid no wider than 80.
        while True:
            min_x, max_x, *_ = size(sky)
            if max_x - min_x < 80:
                print(render(sky))
                break
            elapsed = move(sky, elapsed)

        # At this point the end-user can decide if the points in the sky say something or not
        while input("\nKeep going? "):
            elapsed = move(sky, elapsed)
            print(render(sky))
        return elapsed

    # Non interactive mode is for integration testing and only runs a fixed number of moves
    for _ in range(num_moves):
        move(sky)

    return render(sky)


def part2(file):
    return part1(file)


def move(sky, time=0):
    for p in sky:
        p.move()
    return time + 1


def size(sky):
    return min(p.x() for p in sky),\
        max(p.x() for p in sky),\
        min(p.y() for p in sky),\
        max(p.y() for p in sky)


def render(sky):
    min_x, max_x, min_y, max_y = size(sky)

    buffer = StringIO()
    with redirect_stdout(buffer):
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                if (x, y) in sky:
                    print("#", end='')
                else:
                    print(".", end='')
            print("")

    return buffer.getvalue()


def points(file):
    for line in file:
        px, py, vx, vy = map(int, re.findall(r"[\d-]+", line))
        yield Point((px, py), (vx, vy))


class Point:
    def __init__(self, position, velocity):
        self._position = position
        self._velocity = velocity

    def __eq__(self, other):
        return self._position == other

    def x(self):
        return self._position[0]

    def y(self):
        return self._position[1]

    def move(self):
        self._position = self._position[0] + self._velocity[0], self._position[1] + self._velocity[1]
