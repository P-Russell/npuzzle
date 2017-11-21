import create
from data_from_fd import puzzle_from_fd


class Data(object):

    def __init__(self, size=0, fd=0):
        if size:
            self.size = int(size)
            self.puzzle = create.generate_new(self.size)
        elif fd:
            self.size, self.puzzle = puzzle_from_fd(fd)


class Node(object):

    def __init__(self, data, ):
        self.data = data


    def gen_new(self):
        # generates list of new Nodes