import re


def load_file(file: str):
    lines = []
    rules = {}
    done_rules = False

    # just load all the lines
    with open(file, 'r') as reader:
        for line in reader:
            clean = line.strip()
            if clean == '':
                done_rules = True
                continue

            if not done_rules:
                m = re.match(r'(\d+): (.*)', clean)
                rules[m.group(1)] = m.group(2)
            else:
                lines.append(clean)
    return rules, lines


def combine(a, b):
    if len(a) == 0:
        return b
    if len(b) == 0:
        return a

    combined = set()
    for i in a:
        for n in b:
            combined.add(i + n)
    return combined


def build_rule(rule, rules, mem):
    # already determined
    if rule in mem:
        return mem[rule]

    # found base string
    if rules[rule][0] == '"':
        m = re.match(r'"(\w+)"', rules[rule])
        mem[rule] = set(m.group(1))
        return mem[rule]

    # evaluate rule
    s = set()
    total = set()
    # rules separated by pipe are just unioned
    sub_rules = rules[rule].split(' | ')

    for sub_rule in sub_rules:
        s = set()
        for char in sub_rule.split(' '):
            # other rules need to be combined
            s = combine(s, build_rule(char, rules, mem))
        total = total.union(s)

    return total


def build_rule_two(rule, rules, mem, max_len):
    # already determined
    if rule in mem:
        return mem[rule]

    # found base string
    if rules[rule][0] == '"':
        m = re.match(r'"(\w+)"', rules[rule])
        mem[rule] = set(m.group(1))
        return mem[rule]

    # evaluate rule
    s = set()
    total = set()
    # rules separated by pipe are just unioned
    sub_rules = rules[rule].split(' | ')

    for sub_rule in sub_rules:
        s = set()
        for char in sub_rule.split(' '):
            # other rules need to be combined
            if char == '8':
                # print('LONGEST', max([len(rule) for rule in s]))
                # while max([len(rule) for rule in s]) < max_len:
                #     s = combine(build_rule('42', rules, mem), s)

                #     print('LONGEST', max([len(rule) for rule in s]))
                continue
            if char == '11':
                continue
            s = combine(s, build_rule_two(char, rules, mem, max_len))
            print('the longest rule in set is ',
                  max([len(rule) for rule in s]))
        total = total.union(s)

    return total


def day_nineteen_part_one(file: str):
    rules, lines = load_file(file)
    mem = {}  # keep track of the rules already evaluated

    for rule in rules:
        mem[rule] = build_rule(rule, rules, mem)

    print(sum([1 if line in mem['0'] else 0 for line in lines]))


# maybe we can just keep building to the max length?
def day_nineteen_part_two(file: str):
    rules, lines = load_file(file)
    mem = {}  # keep track of the rules already evaluated
    max_len = max([len(line) for line in lines])
    print('longest string', max_len)

    for rule in rules:
        mem[rule] = build_rule(rule, rules, mem)

    print(sum([1 if line in mem['0'] else 0 for line in lines]))

    # second pass, modify rule 8, 11
    rules['8'] = '42 | 42 8'
    rules['11'] = '42 31 | 42 11 31'

    print('RULE 8', mem['8'])
    print(mem['42'])
    print(combine(mem['42'], mem['42']))
    del mem['8']
    del mem['11']
    del mem['0']

    for rule in rules:
        if rule == '0':
            continue
        mem[rule] = build_rule_two(rule, rules, mem, max_len)

    print('RULE 8', mem['8'])
    mem['0'] = build_rule('0', rules, mem)

    print(sum([1 if line in mem['0'] else 0 for line in lines]))


day_nineteen_part_one('19-example.in')
day_nineteen_part_one('19.in')
day_nineteen_part_two('19-example2.in')
