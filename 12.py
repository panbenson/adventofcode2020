import re
import math


def load_file(file: str):
    lines = []
    # just load all the lines
    with open(file, 'r') as reader:
        lines = [line.strip() for line in reader]

    return lines


def day_twelve_part_one(file: str):
    lines = load_file(file)
    heading = 0  # facing east initially
    dx = 0
    dy = 0
    deg_to_rad = math.pi / 180
    for line in lines:
        m = re.match(r'(\w)(\d+)', line)
        action = m.group(1)
        value = int(m.group(2))

        if action == 'F':
            dx += math.cos(heading) * value
            dy += math.sin(heading) * value
        elif action == 'N':
            dy += value
        elif action == 'S':
            dy -= value
        elif action == 'E':
            dx += value
        elif action == 'W':
            dx -= value
        elif action == 'L':
            heading += value * deg_to_rad
        elif action == 'R':
            heading -= value * deg_to_rad

    print(abs(dx) + abs(dy))


def day_twelve_part_two(file: str):
    lines = load_file(file)
    heading = 0  # facing east initially
    wx = 10
    wy = 1
    dx = 0
    dy = 0
    deg_to_rad = math.pi / 180
    for line in lines:
        m = re.match(r'(\w)(\d+)', line)
        action = m.group(1)
        value = int(m.group(2))

        if action == 'F':
            dx += value * wx
            dy += value * wy
        elif action == 'N':
            wy += value
        elif action == 'S':
            wy -= value
        elif action == 'E':
            wx += value
        elif action == 'W':
            wx -= value
        # rotate a point
        elif action == 'L':
            prev_x, prev_y = wx, wy
            wx = prev_x * math.cos(value * deg_to_rad) - \
                prev_y * math.sin(value * deg_to_rad)
            wy = prev_x * math.sin(value * deg_to_rad) + \
                prev_y * math.cos(value * deg_to_rad)
        elif action == 'R':
            prev_x, prev_y = wx, wy
            wx = prev_x * math.cos(-value * deg_to_rad) - \
                prev_y * math.sin(-value * deg_to_rad)
            wy = prev_x * math.sin(-value * deg_to_rad) + \
                prev_y * math.cos(-value * deg_to_rad)

    print(abs(dx) + abs(dy))


day_twelve_part_one('12-example.in')
day_twelve_part_one('12.in')
day_twelve_part_two('12-example.in')
day_twelve_part_two('12.in')
