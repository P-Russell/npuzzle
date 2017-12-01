from heuristic import get_xy

def in_correct_col(col_num, value, goal):
    size = len(goal)
    y = 0
    while y < size:
        if goal[y][col_num] == value:
            return True
        y += 1
    return False

# Function slightly faster but still buggy
# def cal_conflics(rows, columns, square):
#     size = len(rows)
#     y = 0
#     total = 0
#
#     while y < size:
#         x = 0
#         while x < size:
#             row_delta = rows[y][x]
#             col_delta = columns[y][x]
#             if row_delta != 0 and row_delta != square and row_delta > 0:
#                 while row_delta:
#                     if rows[y][x + row_delta] != square and rows[y][x + row_delta] < rows[y][x]:
#                         total += 1
#                     row_delta -= 1
#             if row_delta != 0 and row_delta != square and row_delta < 0:
#                 while row_delta:
#                     if rows[y][x + row_delta] != square and rows[y][x + row_delta] > rows[y][x]:
#                         total += 1
#                     row_delta -= 1
#             if col_delta != 0 and col_delta != square and col_delta > 0:
#                 while col_delta:
#                     if rows[y + col_delta][x] != square and rows[y + col_delta][x] < columns[y][x]:
#                         total += 1
#                     col_delta -= 1
#             if col_delta != 0 and col_delta != square and col_delta > 0:
#                 while col_delta:
#                     if rows[y + col_delta][x] != square and rows[y + col_delta][x] > columns[y][x]:
#                         total += 1
#                     col_delta += 1
#             x += 1
#         y += 1
#     return total

def cal_row_conflicts(grid, square):
    y = 0
    total = 0
    for row in grid:
        x = 0
        for e in row:
            if e != 0 and e != square:
                delta = e
                if delta > 0:
                    while delta:
                        if grid[y][x + delta] != square and grid[y][x + delta] < e:
                            total += 1
                        delta -= 1
                if delta < 0:
                    while delta:
                        if grid[y][x + delta] != square and grid[y][x + delta] > e:
                            total += 1
                        delta += 1
            x += 1
        y += 1
    return total


def cal_col_conflicts(grid, square):
    y = 0
    total = 0
    for row in grid:
        x = 0
        for e in row:
            if e != 0 and e != square:
                delta = e
                if delta > 0:
                    while delta:
                        if grid[y + delta][x] != square and grid[y + delta][x] < e:
                            total += 1
                        delta -= 1
                if delta < 0:
                    while delta:
                        if grid[y + delta][x] != square and grid[y + delta][x] > e:
                            total += 1
                        delta += 1
            x += 1
        y += 1
    return total


def linear_conflict(grid, goal):
    y = 0
    size = len(grid)
    squ = size * size
    row_con = [[squ for i in range (size)] for i in range(size)]
    col_con = [[squ for i in range (size)] for i in range(size)]
    for row in grid:
        x = 0
        for e in row:
            g_x, g_y = get_xy(e, goal)
            if y == g_y and x != g_x:
                row_con[y][x] = g_x - x
            if x == g_x and y != g_y:
                col_con[y][x] = g_y - y
            if x == g_x and y == g_y:
                row_con[y][x], col_con[y][x] = 0, 0
            x += 1
        y += 1
    return (cal_row_conflicts(row_con, squ) + cal_col_conflicts(col_con, squ))