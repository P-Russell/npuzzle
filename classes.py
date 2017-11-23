import create_new
from data_from_fd import puzzle_from_fd


class Data(object):

    def __init__(self, size=0, fd=0):
        if size:
            self.size = int(size)
            self.puzzle = create_new.generate_new(self.size)
        elif fd:
            self.size, self.puzzle = puzzle_from_fd(fd)


class Node(object):

    def __init__(self, data):
        self.data = data

    def expand(self):
        out = []
        new = []
        temp = shift_right()
        if temp:
            new.append(temp)

        for n in new:
            out.append(Node(n))
        return out
