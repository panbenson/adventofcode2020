import re 

def validate(attrs):
    if 'byr' in attrs:
        if int(attrs['byr']) < 1920 or int(attrs['byr']) > 2002:
            return False
    else:
        return False
    if 'iyr' in attrs:
        if int(attrs['iyr']) < 2010 or int(attrs['iyr']) > 2020:
            return False
    else:
        return False
    if 'eyr' in attrs:
        if int(attrs['eyr']) < 2020 or int(attrs['eyr']) > 2030:
            return False
    else:
        return False
    if 'hgt' in attrs:
        test = re.match(r'^(\d+)(cm|in)$', attrs['hgt'])
        if test == None:
            return False
        if (test.group(2) == 'cm' and (int(test.group(1)) < 150 or int(test.group(1)) > 193)) or (test.group(2) == 'in' and (int(test.group(1)) < 59 or int(test.group(1)) > 76)):
            return False
    else:
        return False
    if 'hcl' in attrs:
        test = re.match(r'^#[0-9a-f]{6}$', attrs['hcl'])
        if test == None:
            return False
    else:
        return False
    if 'ecl' in attrs:
        if attrs['ecl'] not in ['amb','blu','brn','gry','grn','hzl','oth']:
            return False
    else:
        return False
    if 'pid' in attrs:
        test = re.match(r'^\d{9}$', attrs['pid'])
        if test == None:
            return False
    else:
        return False


    return True
    
    

def day_four_part_one():
    idx = 0
    count = 0
    required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

    # just load all the lines
    with open('4.in', 'r') as reader:
        lines = [line for line in reader]

    while idx < len(lines):
        attr_list = []

        # keep loading all the lines
        while idx < len(lines) and lines[idx] != '\n':
            attr_list += lines[idx].strip().split(' ')
            idx += 1

        # build a hash to keep track
        attrs = {}
        for attr in attr_list:
            key, val = attr.split(':')
            attrs[key] = val

        # check missing field
        missing = []
        for field in required:
            if field not in attrs:
                missing.append(field)

        if len(missing) == 0 or (len(missing) == 1 and missing[0] == "cid"):
            count += 1

        idx += 1

    return count

def day_four_part_two(file):
    idx = 0
    count = 0
    required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

    # just load all the lines
    with open(file, 'r') as reader:
        lines = [line for line in reader]

    while idx < len(lines):
        attr_list = []

        # keep loading all the lines
        while idx < len(lines) and lines[idx] != '\n':
            attr_list += lines[idx].strip().split(' ')
            idx += 1

        # build a hash to keep track
        attrs = {}
        for attr in attr_list:
            key, val = attr.split(':')
            attrs[key] = val

        if validate(attrs):
            count += 1

        idx += 1

    return count

print(day_four_part_one())
print(day_four_part_two('4-invalid.in'))
print(day_four_part_two('4-valid.in'))
print(day_four_part_two('4.in'))
