#!/usr/bin/env python3


def get_xy(value, matrix):
    y = 0
    for row in matrix:
        if value in row:
            return row.index(value), y
        y += 1


def in_correct_col(col_num, value, goal):
    size = len(goal)
    y = 0
    while y < size:
        if goal[y][col_num] == value:
            return True
        y += 1
    return False


def linear_conflict(grid, goal):
    y = 0
    row_con = []
    col_con = []
    for row in grid:
        x = 0
        for e in row:
            g_x, g_y = get_xy(e, goal)
            if y == g_y and x != g_x:
                row_con.append([e, y, x - g_x])
            if x == g_x and y != g_y:
                col_con.append([e, y, x])
            x += 1
        y += 1
    return row_con, col_con


def cal_conflicts(rows):
    pass

def main():
    goal = [
        [1, 2, 3],
        [4, 0, 8],
        [7, 6, 5]
    ]

    test = [
        [1, 3, 2],
        [7, 0, 4],
        [8, 5, 6]
    ]

    conflicts_rows, conflicts_columns = linear_conflict(test, goal)
    print(conflicts_rows)
   # h = cal_conflicts_rows(conflicts_rows)
    print(conflicts_columns)


if __name__ == '__main__':
    main()
