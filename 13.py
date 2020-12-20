def load_file(file: str):
    lines = []
    # just load all the lines
    with open(file, 'r') as reader:
        lines = [line.strip() for line in reader]

    return (int(lines[0]), lines[1].split(','))


def day_thirteen_part_one(file: str):
    start, busses = load_file(file)
    # ignoring x for now
    busses = list(map(int, filter(lambda x: x != 'x', busses)))

    next_bus = start
    bus = None

    # maybe just loop thru all the possible values
    while bus == None:
        for i in busses:
            if next_bus % i == 0:
                bus = i
                break
        if bus == None:
            next_bus += 1

    print((next_bus - start) * bus)


def day_thirteen_part_two(file: str):
    start, busses = load_file(file)
    # convert int for possible numbers
    busses = list(map(lambda x: int(x) if x != 'x' else x, busses))

    lcm = busses[0]
    # maybe just find when pattern repeats?
    for i in range(1, len(busses)):
        print(lcm, busses[i])
        if busses[i] == 'x':
            continue
        n = 1
        q = (lcm * n + i) // busses[i]

        while lcm * n + i != busses[i] * q:
            if lcm * n + i < busses[i] * q:
                n += 1
            elif lcm * n + i > busses[i] * q:
                q += 1

        # print(lcm * n)
        lcm *= n

    print(lcm)


def valid(busses, multiples):
    # they should all match busses[0] * multiple[0]
    for i in range(1, len(busses)):
        if busses[i] == 'x':
            continue

        if busses[i] * multiples[i] - i != busses[0] * multiples[0]:
            return False

    return True


def day_thirteen_part_two_bf(file: str):
    start, busses = load_file(file)
    # convert int for possible numbers
    busses = list(map(lambda x: int(x) if x != 'x' else x, busses))

    # couldn't math it, just brute force again?
    multiples = [1 for i in range(len(busses))]

    # find the max in list
    multiples_max = 0
    for i in range(len(busses)):
        if busses[i] == 'x':
            continue
        if busses[i] * multiples[i] > multiples_max:
            multiples_max = busses[i] * multiples[i]

    while not valid(busses, multiples):

        # increase the others
        for i in range(len(busses)):
            if busses[i] == 'x':
                continue
            if busses[i] * multiples[i] < multiples_max:
                multiples[i] = multiples_max // busses[i] + 1
                if busses[i] * multiples[i] > multiples_max:
                    multiples_max = busses[i] * multiples[i]
            # while busses[i] * multiples[i] < multiples_max:
            #     multiples[i] += 1

    print(multiples[0] * busses[0])
    # solution: find the first multiple which matches the
    # offset, keep adding otherwise


# day_thirteen_part_one('13-example.in')
# day_thirteen_part_one('13.in')
day_thirteen_part_two_bf('13-short.in')
day_thirteen_part_two_bf('13-example.in')
