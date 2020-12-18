def load_file(file: str):
    lines = []
    # just load all the lines
    with open(file, 'r') as reader:
        lines = [line.strip() for line in reader]

    return lines

def parse(equation, entry):
    idx = entry
    operator = '+'
    result = 0
    while idx < len(equation):
        if equation[idx] == ' ':
            idx += 1 
            continue
        elif equation[idx] == '+' or equation[idx] == '*':
            operator = equation[idx]
        elif equation[idx] == '(':
            val, i = parse(equation, idx + 1)
            idx = i
            result = result + val if operator == '+' else result * val
        elif equation[idx] == ')':
            return result, idx
        else:
            result = result + int(equation[idx]) if operator == '+' else result * int(equation[idx])

        idx += 1
    return result

def parse_2(equation, entry):
    idx = entry
    result = 0
    while idx < len(equation):
        if equation[idx] == ' ' or equation[idx] == '+':
            idx += 1 
            continue
        elif equation[idx] == '*':
            # lower precedence, do first then return
            val, i = parse_2(equation, idx + 1)
            idx = i
            return result * val, idx
        elif equation[idx] == '(':
            val, i = parse_2(equation, idx + 1)
            idx = i
            result = result + val
        elif equation[idx] == ')':
            return result, idx
        else:
            result += int(equation[idx])

        idx += 1
    return result, idx

def day_eighteen_part_one(file: str):
    lines = load_file(file)
    evaluated = [parse(line, 0) for line in lines]
    print(sum(evaluated))

def day_eighteen_part_two(file: str):
    lines = load_file(file)
    evaluated = [parse_2(line, 0)[0] for line in lines]
    print(sum(evaluated))
    

day_eighteen_part_one('18-example.in')
day_eighteen_part_one('18.in')
day_eighteen_part_two('18-example.in')
day_eighteen_part_two('18.in')
