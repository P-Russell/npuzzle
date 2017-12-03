#!/usr/bin/env python3
import math
from snail_gen import gen_snail
import random


def flatten_array(l):
    flat = []
    for row in l:
        for e in row:
            flat.append(e)
    return flat


def create_dict(p_size):
    snail = flatten_array(gen_snail(p_size))
    norm = [x for x in range(1,(p_size ** 2 + 1) )]
    keys = {}
    for k, v in zip(snail, norm):
        keys[k] = v
    return keys


def is_solvable(array, p_size):
    keys = create_dict(p_size)
    inv = inversion(array, keys)
    if p_size % 2 != 0:
        return inv % 2 == 0
    else:
        b_pos = blank_pos_from_bot(array, p_size)
        if b_pos % 2 == 0 and inv % 2 != 0:
            return True
        elif b_pos % 2 != 0 and inv % 2 == 0:
            return True
    return False


def blank_pos_from_bot(array, p_size):
    if 0 in array:
        index = array.index(0) + 1
    return p_size - (math.ceil(index / p_size) - 1)


def inversion(array, diction):
    length = len(array)
    converted = []
    for e in array:
        converted.append(diction[e])
    print('converted ', converted)
    inv_count = 0
    i = 0
    while i < length - 1:
        j = i + 1
        while j < length:
            if converted[i] > converted[j]:
                print('inversion found ', converted[i], converted[j])
                inv_count += 1
            j += 1
        i += 1
    print(converted)
    return inv_count

s = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
    ]

puz =[
    [1, 2, 3],
    [4, 8, 0],
    [7, 5, 6]
]

test_dict = create_dict(3)

test2 = [x for x in range(9)]
test3 = [3, 7, 6, 8, 5, 4, 1, 2, 0]

print(test_dict)
random.shuffle(test2)

#inv = inversion(flatten_array(puz), test)
inv = inversion(test3, test_dict)
print(inv)
