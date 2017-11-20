import create


class Data(object):

    def __init__(self, size=0, fd=0):
        print ("about to create a new ")
        super(Data, self).__init__()
        if size:
            self.size = int(size)
            self.puzzle = create.generate_new(self.size)
        elif fd:
            self.size, self.puzzle = create.puzzle_from_fd(fd)
