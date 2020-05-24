def part1(file):
    """
    O(n * r) time and O(n) space, where n is the number of units in the polymer and r is the number of reactions
    :param file:
    :return:
    """
    polymer = file.single_line()

    return len(react(polymer))


def part2(file):
    """
    O(n * r) time and O(n) space, where n is the number of units in the polymer and r is the number of reactions
    :param file:
    :return:
    """
    polymer = file.single_line()
    length = len(polymer)
    for i in range(65, 91):
        reacted = react(polymer.replace(chr(i), '').replace(chr(i + 32), ''))
        length = min(length, len(reacted))

    return length


def react(polymer):
    polymer = list(polymer)
    left, right = 0, 1
    while True:
        # At end of polymer, no more reactions
        if right == len(polymer):
            break
        # Find reacting pairs
        if polymer[left] != polymer[right] and polymer[left].upper() == polymer[right].upper():
            # Remove them
            polymer.pop(right)
            polymer.pop(left)

            # Backtrack by one
            left, right = max(0, left - 1), max(1, right - 1)
        else:
            # Advance cursors
            left += 1
            right += 1

    return ''.join(polymer)
