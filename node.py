from shift import *

class Node(object):

    def __init__(self, data):
        self.data = data


    def expand(self):
        nodes = []
        tmp = right_shift(self.data)
        if tmp:
            nodes.append(Node(tmp))
        tmp = left_shift(self.data)
        if tmp:
            nodes.append(Node(tmp))
        tmp = up_shift(self.data)
        if tmp:
            nodes.append(Node(tmp))
        tmp = down_shift(self.data)
        if tmp:
            nodes.append(Node(tmp))
        return nodes