from collections import Counter

def day_two_part_one():
    valid = 0
    lines = []

    # just load all the lines
    with open('2.in', 'r') as reader:
        lines = [line.split() for line in reader]

    for line in lines:
        # 0 =  min to max, 1 = character, 2 = password
        min_char, max_char = map(int, line[0].split('-'))
        char = line[1][0]
        count = Counter(line[2])[char]

        if count >= min_char and count <= max_char:
            valid += 1

    return valid

def day_two_part_two():
    valid = 0
    lines = []

    # just load all the lines
    with open('2.in', 'r') as reader:
        lines = [line.split() for line in reader]

    for line in lines:
        # 0 =  indices to indices, 1 = character, 2 = password
        min_char, max_char = map(lambda x: int(x) - 1, line[0].split('-'))
        char = line[1][0]

        if (line[2][min_char] == char) != (line[2][max_char] == char):
            valid += 1

    return valid

# note: just use regex next time i.e. m = re.search(r'(\d+)-(\d+) (\w): (\w+)', '5-9 g: ggccggmgn')
print(day_two_part_one())
print(day_two_part_two())
