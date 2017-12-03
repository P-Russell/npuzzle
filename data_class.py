import create_new
from data_from_fd import puzzle_from_fd
from snail_gen import gen_snail


class Data(object):

    def __init__(self, size=0, fd=0, heuristic=1):
        if size:
            self.size = int(size)
            self.puzzle = create_new.generate_new(self.size)
        elif fd:
            self.size, self.puzzle = puzzle_from_fd(fd)

        if self.size:
            self.goal = gen_snail(self.size)

        self.heuristic = heuristic
