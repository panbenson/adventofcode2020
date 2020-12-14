def load_file(file: str):
    lines = []
    # just load all the lines
    with open(file, 'r') as reader:
        lines = [line.strip() for line in reader]

    return (int(lines[0]), lines[1].split(','))


def next_alignment(bus0, delay0, bus1, delay1):
    base = delay0
    while True:
        # keep adding multiple
        base += bus0
        # if the remainder of this number is the delay, then we are off by idx
        if base % bus1 == delay1:
            return(base)


def y2020_13_part2(data):
    busses = data[1]
    base = 0
    baseid = int(busses[0])
    # build from the first element
    for idx, busid in enumerate(busses[1:], start=1):
        if busid == 'x':
            continue
        busid = int(busid)
        # the multiple we are looking for
        busidx = busid - idx

        # adjust for delays greater than busid
        while busidx < 0:
            busidx += busid

        print(f"call next_alignment: {baseid}, {base}, {busid}, {busidx}")
        # find the value in which first group and next number are off by idx
        alignment = next_alignment(baseid, base, busid, busidx)
        print(f"all busses so far align to {alignment}")
        # to keep this into the next, we multiply them together since
        # pattern would repeat every multiple!
        baseid *= busid
        # then we shift the base number back by this multiple
        base = alignment - baseid
    return alignment


def main():
    lines = load_file('13-short.in')
    print(y2020_13_part2(lines))
    lines = load_file('13.in')
    print(y2020_13_part2(lines))


main()
