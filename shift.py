def right_shift(grid):
    y = 0
    for row in grid:
        if '0' in row:
            x = row.index('0')
            break
        y += 1
    try:
        new = grid.copy()
        temp = new[y][x + 1]
        new[y][x + 1] = '0'
        new[y][x] = temp
        return new
    except IndexError:
        return None


def left_shift(grid):
    new = []
    y = 0
    for row in grid:
        if '0' in row:
            x = row.index('0')
            break
        y += 1
    try:
        new = grid
        temp = new[y][x - 1]
        new[y][x - 1] = '0'
        new[y][x] = temp
        return new
    except IndexError:
        return None


def up_shift(grid):
    new = []
    y = 0
    for row in grid:
        if '0' in row:
            x = row.index('0')
            break
        y += 1
    try:
        new = grid
        temp = new[y - 1][x]
        new[y - 1][x] = '0'
        new[y][x] = temp
        return new
    except IndexError:
        return None


def down_shift(grid):
    new = []
    y = 0
    for row in grid:
        if '0' in row:
            x = row.index('0')
            break
        y += 1
    try:
        new = grid
        temp = new[y + 1][x]
        new[y + 1][x] = '0'
        new[y][x] = temp
        return new
    except IndexError:
        return None
