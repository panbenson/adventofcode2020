from collections import deque
import itertools


def combat(p1, p2):
    while len(p1) and len(p2):
        t1 = p1.popleft()
        t2 = p2.popleft()
        if t1 > t2:
            p1.append(t1)
            p1.append(t2)
        else:
            p2.append(t2)
            p2.append(t1)
    return p1 if len(p1) else p2


def recursive_combat(p1, p2, depth):
    # keep track of played already
    played = set()
    while len(p1) and len(p2):
        if depth == 1:
            print(f'depth: {depth},  {len(played)}')
        hashed = ''.join(list(map(str, p1))) + '|' + \
            ''.join(list(map(str, p2)))
        if hashed in played:
            return (0, p1)
        played.add(hashed)

        t1 = p1.popleft()
        t2 = p2.popleft()
        # recursive combat
        if t1 <= len(p1) and t2 <= len(p2):
            # NEED TO TAKE A SLICE OF THE CARDS... READ THE INSTRUCTIONS
            winner, p = recursive_combat(
                deque(itertools.islice(p1.copy(), 0, t1)), deque(itertools.islice(p2.copy(), 0, t2)), depth + 1)
            if winner == 0:
                p1.append(t1)
                p1.append(t2)
            else:
                p2.append(t2)
                p2.append(t1)
        else:
            if t1 > t2:
                p1.append(t1)
                p1.append(t2)
            else:
                p2.append(t2)
                p2.append(t1)
    return (0, p1) if len(p1) else (1, p2)


def day_twenty_two_part_one():
    example_p1 = deque([9, 2, 6, 3, 1])
    example_p2 = deque([5, 8, 4, 7, 10])
    p1 = deque([
        40, 26, 44, 14, 3, 17, 36, 43, 47, 38, 39, 41, 23, 28, 49, 27, 18, 2, 13, 32, 29, 11, 25, 24, 35
    ])
    p2 = deque([
        19, 15, 48, 37, 6, 34, 8, 50, 22, 46, 20, 21, 10, 1, 33, 30, 4, 5, 7, 31, 12, 9, 45, 42, 16
    ])

    winning_hand = combat(p1, p2)
    print(winning_hand)
    print(sum([winning_hand[i] * (len(winning_hand) - i)
               for i in range(len(winning_hand))]))


def day_twenty_two_part_two():
    example_p1 = deque([9, 2, 6, 3, 1])
    example_p2 = deque([5, 8, 4, 7, 10])
    p1 = deque([
        40, 26, 44, 14, 3, 17, 36, 43, 47, 38, 39, 41, 23, 28, 49, 27, 18, 2, 13, 32, 29, 11, 25, 24, 35
    ])
    p2 = deque([
        19, 15, 48, 37, 6, 34, 8, 50, 22, 46, 20, 21, 10, 1, 33, 30, 4, 5, 7, 31, 12, 9, 45, 42, 16
    ])
    infinite_p1 = deque([43, 19])
    infinite_p2 = deque([2, 29, 14])

    i, winning_hand = recursive_combat(p1, p2, 1)
    print(winning_hand)
    print(sum([winning_hand[i] * (len(winning_hand) - i)
               for i in range(len(winning_hand))]))


day_twenty_two_part_one()
day_twenty_two_part_two()
