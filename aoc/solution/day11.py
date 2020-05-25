def part1(file):
    """
    O(n^2) time and space where n is the size of the grid
    :param file:
    :return:
    """
    serial_number = int(file.single_line())
    grid = []
    # Populate a 300x300 grid with power level values
    for y in range(300):
        grid.append([])
        for x in range(300):
            grid[y].append(power_level(x, y, serial_number))

    # Find the most powerful 3x3 square
    most_powerful = (None, 0)
    for y in range(298):
        for x in range(298):
            square_power = sum(grid[ny][nx] for nx, ny in square(x, y))
            if square_power > most_powerful[1]:
                most_powerful = (x, y), square_power

    return f"{most_powerful[0][0]},{most_powerful[0][1]}"


def part2(file):
    """
    O(n^3) time and O(n^2) space where n is the size of the grid
    :param file:
    :return:
    """
    serial_number = int(file.single_line())
    grid = []
    # Populate a 300x300 grid as a summed-area table of power level values
    for y in range(300):
        grid.append([])
        for x in range(300):
            square_power = power_level(x, y, serial_number)
            if x > 0:
                square_power += grid[y][x-1]
            if y > 0:
                square_power += grid[y-1][x]
            if y > 0 and x > 0:
                square_power -= grid[y-1][x-1]
            grid[y].append(square_power)

    most_powerful = (None, 0, 0)
    for y in range(300):
        max_height = 300 - y
        for x in range(300):
            max_width = 300 - x
            # Don't fetch a square that would extend outside the grid
            for size in range(1, min(max_width, max_height)):
                if size == 1:
                    square_power = grid[y][x]
                else:
                    # Summed-area table calculation of square's power level
                    square_power = grid[y+size-1][x+size-1]
                    if x > 0:
                        square_power -= grid[y+size-1][x - 1]
                    if y > 0:
                        square_power -= grid[y-1][x+size-1]
                    if y > 0 and x > 0:
                        square_power += grid[y-1][x-1]
                if square_power > most_powerful[1]:
                    most_powerful = (x, y), square_power, size

    return f"{most_powerful[0][0]},{most_powerful[0][1]},{most_powerful[2]}"


def square(x, y, size=3):
    for x_offset in range(x, x + size):
        for y_offset in range(y, y + size):
            yield (x_offset, y_offset)


def power_level(x, y, sn):
    rack_id = x + 10
    level = (rack_id * y + sn) * rack_id
    hundreds = int(str(level)[-3])
    return hundreds - 5
