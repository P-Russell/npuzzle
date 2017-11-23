import random
from is_solvable import is_solvable


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
    return shape(new, size)
