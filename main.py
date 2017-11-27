#!/usr/bin/env python3

from data_class import *
import sys
from solve import a_star


def main():
    data = None
    if len(sys.argv) == 2:
        try:
            fd = open(sys.argv[1], 'r')
            data = Data(fd=fd)
            fd.close()
        except OSError:
            if sys.argv[1].isdigit() and int(sys.argv[1]) > 1:
                data = Data(sys.argv[1])
            else:
                print("usage: main.py [path to puzzle] OR [size of puzzle to be generated > 1]")
        if data and data.puzzle:
            a_star(data)
    else:
        print("usage: main.py [path to puzzle] OR [size of puzzle to be generated > 1]")


if __name__ == '__main__':
    main()
