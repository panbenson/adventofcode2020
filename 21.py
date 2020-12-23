import re
from collections import defaultdict


def load_file(file: str):
    lines = []

    # just load all the lines
    with open(file, 'r') as reader:
        for line in reader:
            m = re.match(r'([\w\s]+) \(contains ([\w\s,]+)\)', line.strip())
            lines.append((set(m.group(1).split(' ')), m.group(2).split(', ')))

    return lines


def day_twenty_one_part_one(file: str):
    lines = load_file(file)
    allergens = {}
    count = defaultdict(int)
    no_allergies = 0
    for line in lines:
        ingredients = line[0]
        contains = line[1]

        # count the ingredients
        for ingredient in ingredients:
            count[ingredient] += 1

        for contain in contains:
            if contain in allergens:
                updated = ingredients.intersection(allergens[contain])
                allergens[contain] = updated
            else:
                allergens[contain] = ingredients

    # set up all the allergens to compare
    all_allergens = set()
    for allergen in allergens:
        all_allergens = all_allergens.union(allergens[allergen])

    # known good
    for allergen in count:
        if allergen not in all_allergens:
            no_allergies += count[allergen]

    print(no_allergies)
    sorted_allergens = sorted([(key, allergens[key])
                               for key in allergens], key=lambda x: len(x[1]))
    mapped = find_allergens(sorted_allergens, set(), {})
    mapped_arr = sorted([(key, mapped[key])
                         for key in mapped], key=lambda x: x[0])
    print(','.join([word[1] for word in mapped_arr]))


def find_allergens(allergens, used, output):
    if not len(allergens):
        return output

    allergen = allergens[0]
    for ingredient in allergen[1]:
        if ingredient in used:
            continue
        new_used = used.copy()
        new_used.add(ingredient)
        output[allergen[0]] = ingredient
        res = find_allergens(allergens[1:], new_used, output)
        if res:
            return output


day_twenty_one_part_one('21-example.in')
day_twenty_one_part_one('21.in')
