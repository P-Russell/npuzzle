from copy import deepcopy


def print_list(l):
    if l:
        print ('------------------------------')
        for row in l:
            for e in row:
                print(str(e), end='\t')
            print()
        print ('------------------------------')


def right_shift(grid):
    y = 0
    x = 0
    for row in grid:
        if 0 in row:
            x = row.index(0)
            break
        y += 1
    try:
        if x > 0:
            new = deepcopy(grid)
            new[y][x] = new[y][x - 1]
            new[y][x - 1] = 0
            return new
        return None
    except IndexError:
        return None


def left_shift(grid):
    y = 0
    x = 0
    for row in grid:
        if 0 in row:
            x = row.index(0)
            break
        y += 1
    try:
        new = deepcopy(grid)
        new[y][x] = new[y][x + 1]
        new[y][x + 1] = 0
        return new
    except IndexError:
        return None


def up_shift(grid):
    y = 0
    x = 0
    for row in grid:
        if 0 in row:
            x = row.index(0)
            break
        y += 1
    try:
        new = deepcopy(grid)
        new[y][x] = new[y + 1][x]
        new[y + 1][x] = 0
        return new
    except IndexError:
        return None


def down_shift(grid):
    y = 0
    x = 0
    for row in grid:
        if 0 in row:
            x = row.index(0)
            break
        y += 1
    try:
        if y > 0:
            new = deepcopy(grid)
            new[y][x] = new[y - 1][x]
            new[y - 1][x] = 0
            return new
        return None
    except IndexError:
        return None
