import math


def is_solvable(array, p_size):
    inv = inversion(array)
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


def inversion(array):
    length = len(array)
    inv_count = 0
    i = 0
    while i < length - 1:
        j = i + 1
        while j < length:
            if array[i] > array[j]:
                inv_count += 1
            j += 1
        i += 1
    return inv_count
