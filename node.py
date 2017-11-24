from shift import *


def expand_node(grid):
    nodes = []
    tmp = right_shift(grid)
    if tmp:
        nodes.append(Node(tmp))
    tmp = left_shift(grid)
    if tmp:
        nodes.append(Node(tmp))
    tmp = up_shift(grid)
    if tmp:
        nodes.append(Node(tmp))
    tmp = down_shift(grid)
    if tmp:
        nodes.append(Node(tmp))
    return nodes


def get_xy(value, matrix):
    y = 0
    for row in matrix:
        if value in row:
            return row.index(value), y
        y += 1

# def get_xy(value, matrix):
#     y = 0
#     for row in matrix:
#         x = 0
#         for e in row:
#             if e == value:
#                 return x, y
#             x += 1
#         y += 1

def man_dist(grid, goal):
    h = 0

    x = 0
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


class Node(object):

    h = 999

    def __init__(self, data):
        self.data = data

    def man_h(self, goal):
        self.h = man_dist(self.data, goal)
        return self.h

    def expand(self):
        return expand_node(self.data)