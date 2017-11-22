def print_list(l):
    if l:
        for row in l:
            print (row)


def right_shift(grid):
    y = 0
    for row in grid:
        if '0' in row:
            x = row.index('0')
            break
        y += 1
    try:
        print ('for right shift 0 position y = ' + str(y) + ' x = ' + str(x))
        new = grid[:]
        temp = new[y][x + 1]
        new[y][x + 1] = '0'
        new[y][x] = temp
        return new
    except IndexError:
        return None


def left_shift(grid):
    y = 0
    for row in grid:
        if '0' in row:
            x = row.index('0')
            break
        y += 1
    try:
        new = grid[:]
        temp = new[y][x - 1]
        new[y][x - 1] = '0'
        new[y][x] = temp
        return new
    except IndexError:
        return None


def up_shift(grid):
    y = 0
    for row in grid:
        if '0' in row:
            x = row.index('0')
            break
        y += 1
    try:
        new = grid[:]
        temp = new[y + 1][x]
        new[y + 1][x] = '0'
        new[y][x] = temp
        return new
    except IndexError:
        return None


def down_shift(grid):
    y = 0
    for row in grid:
        if '0' in row:
            x = row.index('0')
            break
        y += 1
    try:
        new = grid[:]
        temp = new[y - 1][x]
        new[y - 1][x] = '0'
        new[y][x] = temp
        return new
    except IndexError:
        return None
