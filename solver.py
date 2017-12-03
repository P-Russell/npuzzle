import math
from snail_gen import gen_snail


def flatten_array(l):
    flat = []
    for row in l:
        for e in row:
            flat.append(e)
    return flat


def create_dict(p_size):
    snail = flatten_array(gen_snail(p_size))
    norm = [x for x in range(1,(p_size ** 2 + 1))]
    #norm.append(0)
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
            return False
        elif b_pos % 2 != 0 and inv % 2 == 0:
            return False
    return True


def blank_pos_from_bot(array, p_size):
    if 0 in array:
        index = array.index(0) + 1
    return p_size - (math.ceil(index / p_size) - 1)


def inversion(array, diction):
    length = len(array)
    converted = []
    for e in array:
        converted.append(diction[e])
    inv_count = 0
    i = 0
    while i < length - 1:
        j = i + 1
        while j < length:
            if converted[i] > converted[j] and diction[0] != converted[i] and diction[0] != converted[j]:
                inv_count += 1
            j += 1
        i += 1
    return inv_count
