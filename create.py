import math
import random


def shape(a, size):
    temp = []
    grid = []
    i = 0
    for e in a:
        if i < size:
            temp.append(e)
            i += 1
        if i == size:
            grid.append(temp)
            temp = []
            i = 0
    return grid


def generate_new(size):
    new = [x for x in range(size * size)]
    random.shuffle(new)
    while not is_solvable(new, size):
        random.shuffle(new)
    return shape(new)


def is_solvable(array, p_size):
    inv = inversion(array)
    print ('inversion = ' + str(inv))
    if p_size % 2 != 0:
        return inv % 2 == 0
    else:
        b_pos = blank_pos_from_bot(array, p_size)
        print ('b_pos = ' + str(b_pos))
        if b_pos % 2 == 0 and inv % 2 != 0:
            return True
        elif b_pos % 2 != 0 and inv % 2 == 0:
            return True
    return False


def blank_pos_from_bot(array, p_size):
    index = array.index('0') + 1
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
