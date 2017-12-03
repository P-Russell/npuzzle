#!/usr/bin/env python3

from data_class import *
import sys
from solve import a_star
import time


def main():
    start_time = time.time()
    data = None
    if len(sys.argv) == 3:
            if sys.argv[2].isdigit() and int(sys.argv[2]) >= 1  and int(sys.argv[2]) <= 3:
                heuristic = int(sys.argv[2])
                try:
                    fd = open(sys.argv[1], 'r')
                    data = Data(fd=fd, heuristic=heuristic)
                    fd.close()
                except OSError:
                    if sys.argv[1].isdigit() and int(sys.argv[1]) > 1:
                        data = Data(sys.argv[1])
                    else:
                        print("usage: main.py [path to puzzle] OR [size of puzzle to be generated > 1] AND "
                              "[1 for Manhattan Distance OR 2 for Hamming Distance OR 3 for Linear conflict]")
                if data and data.puzzle:
                    a_star(data)
            else:
                print("usage: main.py [path to puzzle] OR [size of puzzle to be generated > 1] AND "
                      "[1 for Manhattan Distance OR 2 for Hamming Distance OR 3 for Linear conflict]")
    else:
        print("usage: main.py [path to puzzle] OR [size of puzzle to be generated > 1] AND "
              "[1 for Manhattan Distance OR 2 for Hamming Distance OR 3 for Linear conflict]")
    print("Total runtime %s seconds" % (time.time() - start_time))


if __name__ == '__main__':
    main()
