def get_xy(value, matrix):
    y = 0
    for row in matrix:
        if value in row:
            return row.index(value), y
        y += 1


def man_dist(grid, goal):
    h = 0
    y = 0
    for row in grid:
        x = 0
        for e in row:
            if e != 0:
                goal_x, goal_y = get_xy(e, goal)
                h += abs(goal_x - x) + abs(goal_y - y)
            x += 1
        y += 1
    return h


def ham_dist(grid, goal):
    h = 0
    y = 0
    for row in grid:
        x = 0
        for e in row:
            if e != 0 and e != goal[y][x]:
                h += 1
            x += 1
        y += 1
    return h


# Linear Conflict Tiles Definition: Two tiles tj and tk are in a linear conflict
# if tj and tk are in the same line, the goal positions of tj and tk are both in that
# line, tj is to the right of tk and goal position of tj is to the left of the goal position of tk.
#
# The linear conflict adds at least two moves to the Manhattan Distance of the two conflicting tiles,
# by forcing them to surround one another. Therefore the heuristic function will add a cost of 2 moves
# for each pair of conflicting tiles.


