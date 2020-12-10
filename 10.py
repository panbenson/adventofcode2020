from collections import defaultdict

def load_file(file: str):
    lines = []
    # just load all the lines
    with open(file, 'r') as reader:
        lines = [int(line.strip()) for line in reader]
    return lines

def day_ten_part_one(file: str):
    lines = sorted(load_file(file))
    diff = defaultdict(int)
    prev = 0

    for i in lines:
        diff[i - prev] += 1
        prev = i

    # last one
    diff[3] += 1
    print(diff[1] * diff[3])

def jump(idx: int, lines, memo):
    jump_to = idx + 1
    total = 0

    # made it to the end
    if idx + 1 == len(lines):
        return 1

    while jump_to < len(lines) and lines[jump_to] - lines[idx] <= 3:
        total += memo[jump_to] if jump_to in memo else jump(jump_to, lines, memo)
        jump_to += 1

    # keep track of where you been or else it times out
    memo[idx] = total
    return total


def day_ten_part_two(file: str):
    # looks like that stair problem
    lines = sorted(load_file(file))
    lines.append(lines[-1] + 3)
    lines = [0] + lines
    
    print(jump(0, lines, {}))

day_ten_part_one('10-example.in')
day_ten_part_one('10.in')
day_ten_part_two('10-example1.in')
day_ten_part_two('10-example.in')
day_ten_part_two('10.in')
