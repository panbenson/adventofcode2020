def day_fifteen_part_one(starting_nums):
    spoken = {key: [idx] for idx, key in enumerate(starting_nums)}
    prev_num = starting_nums[-1]
    first_spoken = True
    for i in range(len(starting_nums), 2020):
        # this is a new word/first time spoken
        if len(spoken[prev_num]) == 1:
            prev_num = 0
            spoken[0] = spoken[0] + [i] if 0 in spoken else [i]
        else:
            next_word = spoken[prev_num][-1] - spoken[prev_num][-2]
            spoken[next_word] = spoken[next_word] + [i] if next_word in spoken else [i]
            prev_num = next_word
    print(prev_num)

# need to optimize this <-- just use less memory by keeping the last 2 indices 
def day_fifteen_part_two(starting_nums):
    spoken = {key: [idx] for idx, key in enumerate(starting_nums)}
    prev_num = starting_nums[-1]
    first_spoken = True
    for i in range(len(starting_nums), 30000000):
        if i % 10000 == 0:
            print(f'{i // 10000} / 3000')
        # this is a new word/first time spoken
        if len(spoken[prev_num]) == 1:
            prev_num = 0
            spoken[0] = [spoken[0][-1], i] if 0 in spoken else [i]
        else:
            next_word = spoken[prev_num][-1] - spoken[prev_num][-2]
            spoken[next_word] = [spoken[next_word][-1], i] if next_word in spoken else [i]
            prev_num = next_word

    print(prev_num)


day_fifteen_part_one([0, 3, 6])
day_fifteen_part_one([17,1,3,16,19,0])
# day_fifteen_part_two([0, 3, 6])
day_fifteen_part_two([17,1,3,16,19,0])
