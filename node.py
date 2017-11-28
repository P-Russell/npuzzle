from shift import *
from heuristic import *


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
