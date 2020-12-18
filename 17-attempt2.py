def instantiate_coords(grid):
    active_list = set()
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '#':
                active_list.add((x, y, 0))

    return active_list

def search_list():
    search_list = []
    for z in range(-1, 2):
        for y in range(-1, 2):
            for x in range(-1, 2):
                if x == 0 and y == 0 and z == 0:
                    continue
                search_list.append((x, y, z))
    return search_list

def day_seventeen_part_one():
    example = '''.#.
..#
###'''
    puzzle = '''...#..#.
#..#...#
.....###
##....##
......##
........
.#......
##...#..'''
    parsed_input = [list(row) for row in puzzle.split('\n')]
    # we only care about the active list since changes can only happen
    # at their neighbors
    active_list = instantiate_coords(parsed_input)
    print(active_list)

    for i in range(6):
        new_active_list = set()
        for active in active_list:
            possible_cubes = [(delta[0] + active[0], delta[1] + active[1], delta[2] + active[2]) for delta in search_list()]
            for possible in possible_cubes:
                neighbors = [(delta[0] + possible[0], delta[1] + possible[1], delta[2] + possible[2]) for delta in search_list()]
                active_neighbors = sum([1 if neighbor in active_list else 0 for neighbor in neighbors])
                if possible in active_list:
                    if active_neighbors == 2 or active_neighbors == 3:
                        new_active_list.add(possible)
                else:
                    if active_neighbors == 3:
                        new_active_list.add(possible)

        active_list = new_active_list

    print(len(active_list))
    
def instantiate_coords_two(grid):
    active_list = set()
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '#':
                active_list.add((x, y, 0, 0))

    return active_list

def search_list_two():
    search_list = []
    for w in range(-1, 2):
        for z in range(-1, 2):
            for y in range(-1, 2):
                for x in range(-1, 2):
                    if x == 0 and y == 0 and z == 0 and w == 0:
                        continue
                    search_list.append((x, y, z, w))
    return search_list

def day_seventeen_part_two():
    example = '''.#.
..#
###'''
    puzzle = '''...#..#.
#..#...#
.....###
##....##
......##
........
.#......
##...#..'''
    parsed_input = [list(row) for row in puzzle.split('\n')]
    # we only care about the active list since changes can only happen
    # at their neighbors
    active_list = instantiate_coords_two(parsed_input)
    print(active_list)

    for i in range(6):
        new_active_list = set()
        for active in active_list:
            possible_cubes = [(delta[0] + active[0], delta[1] + active[1], delta[2] + active[2], delta[3] + active[3]) for delta in search_list_two()]
            for possible in possible_cubes:
                neighbors = [(delta[0] + possible[0], delta[1] + possible[1], delta[2] + possible[2], delta[3] + possible[3]) for delta in search_list_two()]
                active_neighbors = sum([1 if neighbor in active_list else 0 for neighbor in neighbors])
                if possible in active_list:
                    if active_neighbors == 2 or active_neighbors == 3:
                        new_active_list.add(possible)
                else:
                    if active_neighbors == 3:
                        new_active_list.add(possible)

        active_list = new_active_list

    print(len(active_list))

# day_seventeen_part_one()
day_seventeen_part_two()
