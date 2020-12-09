def load_file(file: str):
    lines = []
    # just load all the lines
    with open(file, 'r') as reader:
        lines = [int(line.strip()) for line in reader]
    return lines

def two_sum(target, lines):
    nums = set()

    for line in lines:
        num = int(line)
        want = target - num

        if want in nums:
            # return want, num
            return True

        nums.add(num)
    return False

def day_nine_part_one(file: str, premable: int):
    lines = load_file(file)
    idx = premable # start checking on premable

    while idx < len(lines):
        if not two_sum(lines[idx], lines[idx - premable:idx]):
            return lines[idx]
        idx += 1

def day_nine_part_two(file: str, premable: int):
    # this looks like a sliding window q
    lines = load_file(file)
    goal = day_nine_part_one(file, premable)
    left_ptr, right_ptr = 0, 1

    while right_ptr < len(lines):
        # expand the right ptr until valid or equal:
        while sum(lines[left_ptr: right_ptr]) < goal:
            right_ptr += 1

        # finished if equal
        if sum(lines[left_ptr: right_ptr]) == goal and (right_ptr - left_ptr) > 1:
            return lines[left_ptr: right_ptr], min(lines[left_ptr: right_ptr]) + max(lines[left_ptr: right_ptr])

        # else we shrink the left ptr
        while sum(lines[left_ptr: right_ptr]) > goal:
            left_ptr += 1

print(day_nine_part_one('9-example.in', 5))
print(day_nine_part_one('9.in', 25))
print(day_nine_part_two('9-example.in', 5))
print(day_nine_part_two('9.in', 25))
