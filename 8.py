def load_file(file: str):
    lines = []
    # just load all the lines
    with open(file, 'r') as reader:
        lines = [(op[0], int(op[1])) for op in (line.strip().split() for line in reader)]
    return lines


def computer(instr):
    acc = 0
    idx = 0
    history = set()
    loop = False

    while idx < len(instr):
        if idx in history:
            loop = True
            break
        history.add(idx)
        op, val = instr[idx]
        # acc = add or subtract amount to acc and increment idx
        if op == 'acc':
            acc += val
            idx += 1
        # jmp = add or sub amount in idx and execute
        elif op == 'jmp':
            idx += val
        # nop = continue to next instr
        else:
            idx += 1

    if not loop and idx == len(instr):
        return True, acc
    return False, acc

def day_eight_part_one(file: str):
    lines = load_file(file)

    print(computer(lines))

def day_eight_part_two(file: str):
    # one nop is a jmp or one jmp is a nop
    # iterate through all instructions including last one
    lines = load_file(file)
    
    for idx, line in enumerate(lines):
        if line[0] == 'nop' or line[0] == 'jmp':
            lines[idx] = ('jmp', line[1]) if line[0] == 'nop' else ('nop', line[1])
            ok, acc = computer(lines)
            if ok:
                print(acc)
                break
            lines[idx] = ('nop', line[1]) if line[0] == 'nop' else ('jmp', line[1])

day_eight_part_one('8-example.in')
day_eight_part_one('8.in')
day_eight_part_two('8-example.in')
day_eight_part_two('8.in')
