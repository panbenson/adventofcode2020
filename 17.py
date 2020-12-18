def grow(grid):
    ly, lx, lz = len(grid[0]) + 2, len(grid[0][0]) + 2, len(grid) + 2
    front_z = [['.' for i in range(lx)] for n in range(ly)]
    back_z = [['.' for i in range(lx)] for n in range(ly)]

    # grow x and y for grid
    for z in range(lz-2):
        for y in range(ly-2):
            grid[z][y] = ['.'] + grid[z][y] + ['.']
        grid[z] = [['.' for i in range(ly)]] + grid[z] + [['.' for i in range(ly)]]
    
    new_grid = [front_z] + grid + [back_z]
    return new_grid

# shrink if its not used
def shrink(grid):
    # shrink z
    front_z = ''.join([''.join(row) for row in grid[0]]) 
    back_z = ''.join([''.join(row) for row in grid[-1]]) 
    if '#' not in front_z and '#' not in back_z:
        grid = grid[1:-1]

    # shrink y
    front_y = ''.join([''.join(z[0]) for z in grid])
    back_y = ''.join([''.join(z[-1]) for z in grid])
    if '#' not in front_y and '#' not in back_y:
        for z in range(len(grid)):
            grid[z] = grid[z][1:-1]

    # shrink x
    front_x = ''.join([''.join(y[0]) for z in grid for y in z])
    back_x = ''.join([''.join(y[-1]) for z in grid for y in z])
    if '#' not in front_x and '#' not in back_x:
        for z in range(len(grid)):
            for y in range(len(grid[0])):
                grid[z][y] = grid[z][y][1:-1]

    return grid

def determine_next(grid, x, y, z):
    z_p, z_n = z + 1, z - 1
    y_p, y_n = y + 1, y - 1
    x_p, x_n = x + 1, x - 1
    active = 0

    # check z_n
    if z_n >= 0:
        # y_n
        if y_n >= 0:
            if x_n >= 0:
                active += 1 if grid[z_n][y_n][x_n] == '#' else 0
            active += 1 if grid[z_n][y_n][x] == '#' else 0
            if x_p < len(grid[0][0]):
                active += 1 if grid[z_n][y_n][x_p] == '#' else 0
        # y
        if x_n >= 0:
            active += 1 if grid[z_n][y][x_n] == '#' else 0
        active += 1 if grid[z_n][y][x] == '#' else 0
        if x_p < len(grid[0][0]):
            active += 1 if grid[z_n][y][x_p] == '#' else 0
        # y_p
        if y_p < len(grid[0]):
            if x_n >= 0:
                active += 1 if grid[z_n][y_p][x_n] == '#' else 0
            active += 1 if grid[z_n][y_p][x] == '#' else 0
            if x_p < len(grid[0][0]):
                active += 1 if grid[z_n][y_p][x_p] == '#' else 0
    # check z
    if y_n >= 0:
        if x_n >= 0:
            active += 1 if grid[z][y_n][x_n] == '#' else 0
        active += 1 if grid[z][y_n][x] == '#' else 0
        if x_p < len(grid[0][0]):
            active += 1 if grid[z][y_n][x_p] == '#' else 0
    # y
    if x_n >= 0:
        active += 1 if grid[z][y][x_n] == '#' else 0
    # don't check self
    # active += 1 if grid[z][y][x] == '#' else 0
    if x_p < len(grid[0][0]):
        active += 1 if grid[z][y][x_p] == '#' else 0
    # y_p
    if y_p < len(grid[0]):
        if x_n >= 0:
            active += 1 if grid[z][y_p][x_n] == '#' else 0
        active += 1 if grid[z][y_p][x] == '#' else 0
        if x_p < len(grid[0][0]):
            active += 1 if grid[z][y_p][x_p] == '#' else 0
    if z_p < len(grid):
        # y_n
        if y_n >= 0:
            if x_n >= 0:
                active += 1 if grid[z_p][y_n][x_n] == '#' else 0
            active += 1 if grid[z_p][y_n][x] == '#' else 0
            if x_p < len(grid[0][0]):
                active += 1 if grid[z_p][y_n][x_p] == '#' else 0
        # y
        if x_n >= 0:
            active += 1 if grid[z_p][y][x_n] == '#' else 0
        active += 1 if grid[z_p][y][x] == '#' else 0
        if x_p < len(grid[0][0]):
            active += 1 if grid[z_p][y][x_p] == '#' else 0
        # y_p
        if y_p < len(grid[0]):
            if x_n >= 0:
                active += 1 if grid[z_p][y_p][x_n] == '#' else 0
            active += 1 if grid[z_p][y_p][x] == '#' else 0
            if x_p < len(grid[0][0]):
                active += 1 if grid[z_p][y_p][x_p] == '#' else 0
    
    if grid[z][y][x] == '#':
        if active == 2 or active == 3:
            return '#'
        else:
            return '.'
    else:
        if active == 3:
            return '#'
        else:
            return '.'

def print_grid(grid):
    for z in grid:
        print('\n'.join([' '.join(y) for y in z]))
        print()

def count_active(grid):
    print([x for z in grid for y in z for x in y].count('#'))
    # return [x for z in grid for y in z for x in y].count('#')

def day_seventeen_part_one():
    initial_state_example = [
        [
            ['.', '#', '.'],
            ['.', '.', '#'],
            ['#', '#', '#'],
        ]
    ]
    puzzle = [
        [
            ['.','.','.','#','.','.','#','.'],
            ['#','.','.','#','.','.','.','#'],
            ['.','.','.','.','.','#','#','#'],
            ['#','#','.','.','.','.','#','#'],
            ['.','.','.','.','.','.','#','#'],
            ['.','.','.','.','.','.','.','.'],
            ['.','#','.','.','.','.','.','.'],
            ['#','#','.','.','.','#','.','.']
        ]
    ]
    cycle = 6
    for i in range(cycle):
        grid = grow(puzzle)
        new_grid = [[['.' for x in range(len(grid[0][0]))]for y in range(len(grid[0]))] for z in range(len(grid))]
        # count_active(grid)

        for z in range(len(grid)):
            for y in range(len(grid[0])):
                for x in range(len(grid[0][0])):
                    new_grid[z][y][x] = determine_next(grid, x, y, z)

        # print_grid(shrink(new_grid))
        puzzle= new_grid
    count_active(puzzle)

day_seventeen_part_one()
