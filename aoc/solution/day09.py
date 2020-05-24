from collections import deque, defaultdict


def part1(file, last_marble_multiplier=1):
    """
    O(n + p) space and time where p is the number of players
    :param file:
    :param last_marble_multiplier:
    :return:
    """
    num_players, last_marble = parse_input(file)
    current_player = 1
    circle = deque([0])
    scores = defaultdict(lambda: 0)

    for marble in range(1, last_marble_multiplier * last_marble + 1):
        if marble % 23 == 0:
            scores[current_player] += marble
            circle.rotate(7)
            scores[current_player] += circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

        current_player += 1
        if current_player > num_players:
            current_player = 1

    return max(scores.values())


def part2(file):
    return part1(file, 100)


def parse_input(file):
    words = file.single_line().split(' ')
    return int(words[0]), int(words[6])
