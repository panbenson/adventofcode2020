def load_file(file: str):
    lines = []
    # just load all the lines
    with open(file, 'r') as reader:
        lines = [list(line.strip()) for line in reader]

    return lines

# i dont like grid questions :(


def check_seat(x: int, y: int, grid):
    up = y - 1
    down = y + 1
    left = x - 1
    right = x + 1
    occupied = 0

    if grid[y][x] == '.':
        return '.'

    if up >= 0:
        if grid[up][x] == '#':
            occupied += 1
        if left >= 0:
            if grid[up][left] == '#':
                occupied += 1
        if right < len(grid[0]):
            if grid[up][right] == '#':
                occupied += 1
    if down < len(grid):
        if grid[down][x] == '#':
            occupied += 1
        if left >= 0:
            if grid[down][left] == '#':
                occupied += 1
        if right < len(grid[0]):
            if grid[down][right] == '#':
                occupied += 1
    if left >= 0:
        if grid[y][left] == '#':
            occupied += 1
    if right < len(grid[0]):
        if grid[y][right] == '#':
            occupied += 1

    if occupied == 0:
        return '#'
    elif occupied >= 4:
        return 'L'
    else:
        return grid[y][x]


def check_seat_two(x: int, y: int, grid):
    up = y - 1
    down = y + 1
    left = x - 1
    right = x + 1
    occupied = 0

    if grid[y][x] == '.':
        return '.'

    up = y - 1
    if up > -1:
        while up > -1 and grid[up][x] == '.':
            up -= 1
        if up > -1 and grid[up][x] == '#':
            occupied += 1
    up = y - 1
    left = x - 1
    if up > -1 and left >= 0:
        while up > -1 and left >= 0 and grid[up][left] == '.':
            up -= 1
            left -= 1
        if up > -1 and left > -1 and grid[up][left] == '#':
            occupied += 1
    up = y - 1
    right = x + 1
    if up > -1 and right < len(grid[0]):
        while up > -1 and right < len(grid[0]) and grid[up][right] == '.':
            up -= 1
            right += 1
        if up > -1 and right < len(grid[0]) and grid[up][right] == '#':
            occupied += 1

    down = y + 1
    if down < len(grid):
        while down < len(grid) and grid[down][x] == '.':
            down += 1
        if down < len(grid) and grid[down][x] == '#':
            occupied += 1
    down = y + 1
    left = x - 1
    if down < len(grid) and left >= 0:
        while down < len(grid) and left >= 0 and grid[down][left] == '.':
            down += 1
            left -= 1
        if down < len(grid) and left > -1 and grid[down][left] == '#':
            occupied += 1
    down = y + 1
    right = x + 1
    if down < len(grid) and right < len(grid[0]):
        while down < len(grid) and right < len(grid[0]) and grid[down][right] == '.':
            down += 1
            right += 1
        if down < len(grid) and right < len(grid[0]) and grid[down][right] == '#':
            occupied += 1

    left = x - 1
    if left > -1:
        while left > -1 and grid[y][left] == '.':
            left -= 1
        if left > -1 and grid[y][left] == '#':
            occupied += 1
    right = x + 1
    if right < len(grid[0]):
        while right < len(grid[0]) and grid[y][right] == '.':
            right += 1
        if right < len(grid[0]) and grid[y][right] == '#':
            occupied += 1

    if occupied == 0:
        return '#'
    elif occupied >= 5:
        return 'L'
    else:
        return grid[y][x]


def check_seats_two(grid):
    prev = [['' for i in range(len(grid[0]))] for j in range(len(grid))]
    output = grid
    while '\n'.join([''.join(line) for line in prev]) != \
            '\n'.join([''.join(line) for line in output]):
        prev = output
        output = [row[:] for row in output]
        for y in range(len(prev)):
            for x in range(len(prev[0])):
                output[y][x] = check_seat_two(x, y, prev)

    return output


def check_seats(grid):
    prev = [['' for i in range(len(grid[0]))] for j in range(len(grid))]
    output = grid
    while '\n'.join([''.join(line) for line in prev]) != \
            '\n'.join([''.join(line) for line in output]):
        prev = output
        output = [row[:] for row in output]
        for y in range(len(prev)):
            for x in range(len(prev[0])):
                output[y][x] = check_seat(x, y, prev)

    return output


def count_occupied(grid):
    occupied = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '#':
                occupied += 1
    return occupied


def day_eleven_part_one(file: str):
    lines = load_file(file)
    print('\n'.join([''.join(line) for line in lines]))
    new_lines = check_seats(lines)
    print()
    print('\n'.join([''.join(line) for line in new_lines]))
    print(count_occupied(new_lines))


def day_eleven_part_two(file: str):
    lines = load_file(file)
    print('\n'.join([''.join(line) for line in lines]))
    new_lines = check_seats_two(lines)
    print()
    print('\n'.join([''.join(line) for line in new_lines]))
    print(count_occupied(new_lines))


day_eleven_part_one('11-example.in')
day_eleven_part_one('11.in')
day_eleven_part_two('11-example.in')
day_eleven_part_two('11.in')
