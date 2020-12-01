def day_one(target):
    # this looks like a two sum problem
    nums = {}

    with open('1.in', 'r') as reader:
        for line in reader:
            num = int(line)
            want = target - num

            if want in nums:
                return want * num

            nums[num] = 1


def part_two_helper(target, arr):
    nums = {}
    for num in arr:
        want = target - num

        if want in nums:
            return want * num

        nums[num] = 1

# part two, three sum
# we can use 2 sum on sub array


def part_two():
    lines = []
    with open('1.in', 'r') as reader:
        lines = [int(line) for line in reader]

    for i, num in enumerate(lines):
        target = 2020 - num
        val = part_two_helper(target, lines[i + 1:])
        if val != None:
            return num * val


print(day_one(2020))
print(part_two())
