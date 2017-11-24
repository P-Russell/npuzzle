import create_new
from data_from_fd import puzzle_from_fd


class Data(object):

    def gen_snail(self, size):
        ma = size - 1
        snail = [[0 for i in range(size)] for i in range(size)]
        mi = 0
        x = 0
        y = 0
        counter = 1
        snail[y][x] = counter
        counter += 1
        max_count = size * size
        while ma > mi and counter < max_count:
            while x < ma and counter < max_count:
                x += 1
                snail[y][x] = counter
                counter += 1
            while y < ma and counter < max_count:
                y += 1
                snail[y][x] = counter
                counter += 1
            while x > mi and counter < max_count:
                x -= 1
                snail[y][x] = counter
                counter += 1
            mi += 1
            ma -= 1
            while y > mi and counter < max_count:
                y -= 1
                snail[y][x] = counter
                counter += 1
        return snail

    def __init__(self, size=0, fd=0):
        if size:
            self.size = int(size)
            self.puzzle = create_new.generate_new(self.size)
        elif fd:
            self.size, self.puzzle = puzzle_from_fd(fd)

        if self.size:
            self.goal = self.gen_snail(self.size)
