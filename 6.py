from collections import defaultdict


def load_file(file: str):
    # just load all the lines
    with open(file, 'r') as reader:
        lines = [line.strip() for line in reader]

    return lines


def day_six_part_one():
    lines = load_file('6.in')
    counts = []
    counts_sum = 0

    idx = 0
    while idx < len(lines):
        questions = defaultdict(int)

        while idx < len(lines) and lines[idx] != "":
            for question in lines[idx]:
                questions[question] += 1
            idx += 1

        counts.append(questions)
        counts_sum += len(questions)
        idx += 1

    # print(counts)
    print(counts_sum)


def day_six_part_two():
    lines = load_file('6.in')
    counts = []
    counts_sum = 0

    idx = 0
    while idx < len(lines):
        questions = defaultdict(int)
        people = 0

        while idx < len(lines) and lines[idx] != "":
            for question in lines[idx]:
                questions[question] += 1
            people += 1
            idx += 1

        # check which questions everyone answered
        for question in questions:
            if questions[question] == people:
                counts_sum += 1
        idx += 1

    print(counts_sum)


day_six_part_one()
day_six_part_two()
