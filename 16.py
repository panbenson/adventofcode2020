import re
from collections import defaultdict
def load_file(file: str):
    lines = []
    # just load all the lines
    with open(file, 'r') as reader:
        section = 0
        validations = {}
        your_ticket = []
        tickets = []
        for line in reader:
            clean_line = line.strip()
            if clean_line == '':
                section += 1
                continue
            if section == 0:
                m = re.match(r'([\w|\s]+): (\d+-\d+) or (\d+-\d+)', clean_line)
                validations[m.group(1)] = [list(map(int, m.group(2).split('-'))), \
                    list(map(int,m.group(3).split('-')))]
            if section == 1:
                if clean_line == "your ticket:":
                    continue
                your_ticket = list(map(int,clean_line.split(',')))
            if section == 2:
                if clean_line == "nearby tickets:":
                    continue
                tickets.append(list(map(int,clean_line.split(','))))

    return validations, your_ticket, tickets

def merge_intervals(intervals):
    prev = intervals[0]
    merged = []
    for interval in intervals[1:]:
        if interval[0] <= prev[1]:
            prev[1] = max(prev[1], interval[1])
        else:
            merged.append(prev)
            prev = interval
    merged.append(prev)
    return merged

def day_sixteen_part_one(file: str):
    data = load_file(file)
    # do part one as a merge interval q
    intervals = merge_intervals(sorted([item for key in data[0] for item in data[0][key]]))
    invalid = []

    for ticket in data[2]:
        for num in ticket:
            # check if valid for any interval
            valid = False
            for interval in intervals:
                if num >= interval[0] and num <= interval[1]:
                    valid = True
            # if not valid for any interval
            if not valid:
                invalid.append(num)

    print(sum(invalid))
            
def day_sixteen_part_two(file: str):
    data = load_file(file)
    data2 = load_file(file)
    # do part one as a merge interval q
    intervals = data[0]
    merged_intervals = merge_intervals(sorted([item for key in data2[0] for item in data2[0][key]]))
    valid_tickets = []

    ### remove invalid tickets
    for ticket in data[2]:
        include_ticket = True
        for num in ticket:
            # check if valid for any interval
            valid = False
            for interval in merged_intervals:
                if num >= interval[0] and num <= interval[1]:
                    valid = True
            # if not valid for any interval
            if not valid:
                include_ticket = False
                break
        if include_ticket:
            valid_tickets.append(ticket)

    possible_columns = []
    all_possible = set(intervals)
    # check the columns 
    for col in range(len(valid_tickets[0])):
        col_vals = [row[col] for row in valid_tickets]
        not_possible = set()
        for num in col_vals:

            for ticket_type in intervals:
                # check if valid for any interval in type
                valid = False
                for interval in intervals[ticket_type]:
                    if num >= interval[0] and num <= interval[1]:
                        valid = True

                if not valid:
                    not_possible.add(ticket_type)

        possible_columns.append((col, all_possible.difference(not_possible)))

    possible_columns = sorted(possible_columns, key=lambda x: len(x[1]))
    ticket_map = find_order(possible_columns, {})
    # solution
    prod = 1
    for key in ticket_map:
        if 'departure' in key:
            prod *= data[1][ticket_map[key]]
    print(prod)
    

def find_order(possible_columns, order):
    if len(possible_columns) == 0:
        return order
    # try all combos starting from the most likely rows
    for val in possible_columns[0][1]:
        if val in order:
            continue
        new_order = order.copy()
        new_order[val] = possible_columns[0][0]
        recurse = find_order(possible_columns[1:], new_order)
        if recurse:
            return recurse
    return


day_sixteen_part_one('16-example.in')
day_sixteen_part_one('16.in')
day_sixteen_part_two('16-example.in')
day_sixteen_part_two('16-example2.in')
day_sixteen_part_two('16.in')
