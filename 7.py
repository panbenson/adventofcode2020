import re

class Bag:
    def __init__(self, color: str, contains):
        self.color = color
        self.contains = contains if contains is not None else []

def load_file(file: str):
    # just load all the lines
    with open(file, 'r') as reader:
        lines = {}
        # process the lines a bit
        for line in reader:
            m = re.search(r'([\w\s]+) bags contain (.*)', line)
            if m.group(2) == "no other bags.":
                lines[m.group(1)] = {} # lines.append(Bag(m.group(1)))
            else:
                contains = {}
                for bag in m.group(2).split(', '):
                    m_bag = re.search(r'(\d+) ([\w\s]+) bags?', bag)
                    contains[m_bag.group(2)] = int(m_bag.group(1))
                    # contains.append((m_bag.group(1), Bag()))
                lines[m.group(1)] = contains

    return lines

def dfs(bags, color, contains_gold):
    if color in contains_gold or color == "shiny gold":
        return True
    
    has_gold = False
    for sub_color in bags[color]:
        has_gold = has_gold or dfs(bags, sub_color, contains_gold)

    if has_gold:
        contains_gold.add(color)

    return has_gold


def day_seven_part_one(file):
    bags = load_file(file)
    contains_gold = set()
    # this seems like a tree traversal question
    for color in bags:
        dfs(bags, color, contains_gold)

    print(len(contains_gold))

def find_total_bags(bags, color):
    total = 0
    for sub_color in bags[color]:
        total += bags[color][sub_color] + \
            bags[color][sub_color] * find_total_bags(bags, sub_color)
    return total

def day_seven_part_two(file):
    bags = load_file(file)
    print(find_total_bags(bags, 'shiny gold'))

day_seven_part_one('7-example.in')
day_seven_part_one('7.in')
day_seven_part_two('7-example.in')
day_seven_part_two('7.in')
