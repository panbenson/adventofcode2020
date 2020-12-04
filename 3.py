import math

def day_three_part_one(x_inc, y_inc):
    count = 0
    x = x_inc
    y = y_inc

    # just load all the lines
    with open('3.in', 'r') as reader:
        lines = [line for line in reader]

    while y < len(lines):
        if lines[y][x] == '#':
            count += 1
        y += y_inc
        x = (x + x_inc) % (len(lines[0]) - 1) # edge case: since len(lines[0]) should be 0!

    return count

def day_three_part_two():
    tobbogans = []
    tobbogans.append(day_three_part_one(1, 1))
    tobbogans.append(day_three_part_one(3, 1))
    tobbogans.append(day_three_part_one(5, 1))
    tobbogans.append(day_three_part_one(7, 1))
    tobbogans.append(day_three_part_one(1, 2))
    return math.prod(tobbogans)


print(day_three_part_one(3, 1))
print(day_three_part_two())
