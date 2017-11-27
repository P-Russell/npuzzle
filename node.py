from shift import *


def expand_node(grid, parent, goal):
    nodes = []
    tmp = right_shift(grid)
    if tmp:
        nodes.append(Node(tmp, parent, goal))
    tmp = left_shift(grid)
    if tmp:
        nodes.append(Node(tmp, parent, goal))
    tmp = up_shift(grid)
    if tmp:
        nodes.append(Node(tmp, parent, goal))
    tmp = down_shift(grid)
    if tmp:
        nodes.append(Node(tmp, parent, goal))
    return nodes


def get_xy(value, matrix):
    y = 0
    for row in matrix:
        if value in row:
            return row.index(value), y
        y += 1


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

    def __init__(self, data, parent, goal):
        self.data = data
        self.parent = parent
        if parent:
            self.g = parent.g + 1
        else:
            self.g = 0
        self.h = man_dist(self.data, goal)
        self.f = self.g + self.h

    def expand(self, goal):
        return expand_node(self.data, self, goal)
