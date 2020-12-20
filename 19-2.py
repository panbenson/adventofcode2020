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


def build_rule(rule, rules, mem):
    # already determined
    if rule in mem:
        return mem[rule]

    # found base string
    if rules[rule][0] == '"':
        m = re.match(r'"(\w+)"', rules[rule])
        mem[rule] = m.group(1)
        return mem[rule]

    # PART TWO OVERRIDES
    if rule == '8':
        mem[rule] = build_rule('42', rules, mem) + '+'
        return mem[rule]
    if rule == '11':
        fourtytwo = build_rule('42', rules, mem)
        thirtyone = build_rule('31', rules, mem)
        mem[rule] = '(' + '|'.join([fourtytwo +
                                    f'{{{i}}}' + thirtyone + f'{{{i}}}' for i in range(1, 100)]) + ')'
        return mem[rule]
    # END PART TWO OVERRIDES

    # evaluate rule
    sub_rules = rules[rule].split(' | ')

    total = []
    for sub_rule in sub_rules:
        s = ''
        for char in sub_rule.split(' '):
            # other rules need to be combined
            s += build_rule(char, rules, mem)
        total.append(s)

    # build regex's instead :D
    mem[rule] = '(' + '|'.join(total) + ')'

    return mem[rule]


def day_nineteen_part_one(file: str):
    rules, lines = load_file(file)
    mem = {}  # keep track of the rules already evaluated

    for rule in rules:
        mem[rule] = build_rule(rule, rules, mem)

    # print(mem['0'])
    print(sum([1 if bool(re.fullmatch(mem['0'], line)) else 0 for line in lines]))


# day_nineteen_part_one('19-example.in')
# day_nineteen_part_one('19.in')
day_nineteen_part_one('19-example2.in')
day_nineteen_part_one('19.in')
