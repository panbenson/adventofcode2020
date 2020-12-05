def load_file(file: str):
    # just load all the lines
    with open(file, 'r') as reader:
        lines = [line.strip() for line in reader]

    return lines


def day_six_part_one():
    lines = load_file('6.in')
