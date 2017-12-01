from shift import *
from heuristic import *
from linear import linear_conflict


def expand_node(grid, parent, goal, heuristic):
    nodes = []
    tmp = right_shift(grid)
    if tmp:
        nodes.append(Node(tmp, parent, goal, heuristic))
    tmp = left_shift(grid)
    if tmp:
        nodes.append(Node(tmp, parent, goal, heuristic))
    tmp = up_shift(grid)
    if tmp:
        nodes.append(Node(tmp, parent, goal, heuristic))
    tmp = down_shift(grid)
    if tmp:
        nodes.append(Node(tmp, parent, goal, heuristic))
    return nodes


class Node(object):

    def __init__(self, data, parent, goal, heuristic):
        self.data = data
        self.parent = parent
        self.heuristic = heuristic
        if parent:
            self.g = parent.g + 1
        else:
            self.g = 0
        if self.heuristic == 1:
            self.h = man_dist(self.data, goal)
        if self.heuristic == 2:
            self.h = ham_dist(self.data, goal)
        if self.heuristic == 3:
            self.h = man_dist(self.data, goal) + linear_conflict(self.data, goal)
        self.f = self.g + self.h

    def expand(self, goal):
        return expand_node(self.data, self, goal, self.heuristic)
