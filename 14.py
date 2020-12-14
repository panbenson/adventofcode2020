import re

def load_file(file: str):
    lines = []
    # just load all the lines
    with open(file, 'r') as reader:
        # lines = [line.strip() for line in reader]
        instructions = []
        # do some processing
        for line in reader:
            mask_m = re.match(r'mask = (\w+)', line.strip())
            if mask_m != None:
                instructions.append((-1, mask_m.group(1)))
            else:
                ins = re.match(r'mem\[(\d+)\] = (\d+)', line.strip())
                instructions.append((int(ins.group(1)), int(ins.group(2))))

    return instructions


def day_fourteen_part_one(file: str):
    lines = load_file(file)
    # we can do a bitwise and manually
    mask = ''
    values = {}
    for line in lines:
        # reading a new mask
        if line[0] == -1:
            mask = line[1]
        else:
            s = ''
            for i, char in enumerate(list(format(line[1], '036b'))):
                # take value for all mask == 'X'
                s += char if mask[i] == 'X' else mask[i]

            # write value to address
            values[line[0]] = int(s, 2)
            
    print(sum([values[i] for i in values]))

def day_fourteen_part_two(file: str):
    lines = load_file(file)
    # we can do a bitwise and manually
    mask = ''
    floating_idx = []
    values = {}
    for line in lines:
        # reading a new mask
        if line[0] == -1:
            mask = line[1]
            floating_idx = []
            # need to count the X's
            for i, char in enumerate(list(mask)):
                if char == 'X':
                    floating_idx.append(i)
        else:
            s = ''
            # find the base address
            for i, char in enumerate(list(format(line[0], '036b'))):
                # no change for mask == 0
                s += char if mask[i] == '0' else mask[i]
            # go thru all the permutations
            for combo_val in range(2 ** len(floating_idx)):
                new_mask = list(s)
                combo = list(format(combo_val, f'0{len(floating_idx)}b'))
                # apply permutation to mask
                for i, idx in enumerate(floating_idx):
                    new_mask[idx] = combo[i]

                # write value to address
                values[int(''.join(new_mask), 2)] = line[1]
        
    print(sum([values[i] for i in values]))

day_fourteen_part_one('14-example.in')
day_fourteen_part_one('14.in')
day_fourteen_part_two('14-example2.in')
day_fourteen_part_two('14.in')

