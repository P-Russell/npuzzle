#!/usr/bin/env python3

from shift import print_list


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


def cal_conflicts(rows, size):
    i = 0
    conflicts = 0
    grid = []
    while i < size:
        h = list(filter(lambda x: x[1] == i, rows))
        grid.append(h)
        i += 1
    for row in grid:
        while len(row) > 2:
            current = row.pop()
            for e in row:
                if current[2] > 0:
                    if e[2] < 0:
                        conflicts += 1
                else:
                    if e[2] > 0:
                        conflicts += 1


def main():
    goal = [
        [1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 0, 15, 6],
        [10, 9, 8, 7]
    ]

    test = [
        [1, 4, 3, 5],
        [12, 13, 14, 2],
        [11, 0, 15, 6],
        [10, 9, 7, 8]
    ]
    size = len(test)
    conflicts_rows, conflicts_columns = linear_conflict(test, goal)
    print(conflicts_rows)
    #h = cal_conflicts(conflicts_rows, size)
    #print(conflicts_columns)


if __name__ == '__main__':
    main()
