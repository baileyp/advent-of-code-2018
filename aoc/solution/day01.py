from builtins import sum, zip


def part1(file):
    return sum(int(line) for line in file)


def part2(file):
    frequency = 0
    found = {frequency}

    for line in file.iter_infinite():
        frequency += int(line)
        if frequency in found:
            return frequency
        found.add(frequency)

    return None
