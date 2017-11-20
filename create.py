import math
import random


def generate_new(size):
    new = [x for x in range(size * size)]
    random.shuffle(new)
    while not is_solvable(new, size):
        random.shuffle(new)
    return new


def is_solvable(array, p_size):
    inver = cal_inversion(array)
    if p_size % 2 != 0:
        return inver % 2 == 0
    else:
        b_pos = blank_pos_from_bot(array, p_size)
        if b_pos % 2 == 0 and inver % 2 != 0:
            return True
        elif b_pos % 2 != 0 and inver % 2 == 0:
            return True
    return False


def blank_pos_from_bot(array, p_size):
    index = array.index(0) + 1
    return p_size - (math.ceil(index / p_size) - 1)


def cal_inversion(array):
    length = len(array)
    inver_count = 0
    i = 0
    while i < length - 1:
        j = i + 1
        while j < length:
            if array[i] > array[j]:
                inver_count += 1
            j += 1
        i += 1
    return inver_count


def valid_data(size, grid):
    if size != len(grid):
        print ("Problem with puzzle data in " + fd.name)


def puzzle_from_fd(fd):
    line = fd.readline().rstrip()
    grid = []
    if line.isdigit():
        size = int(line)
    else:
        print ("First line of file " + fd.name + " needs to be puzzle size")
        return None, None
    line = fd.readline()
    while line:
        line = line.partition('#')[0].rstrip()
        grid.append(line.split())
        print ("------ " + line)
        line = fd.readline()
    if valid_data(size, grid):
        return size, grid
    else:
        print()
