#!/usr/bin/env python3


from classes import *
import sys
from shift import print_list
from solve import solve


def main():
    data = None
    if len(sys.argv) == 2:
        try:
            fd = open(sys.argv[1], 'r')
            data = Data(fd=fd)
            fd.close()
        except OSError:
            if sys.argv[1].isdigit():
                data = Data(sys.argv[1])
            else:
                print ( "usage: main.py [path to puzzle] OR [number for size of "
                        "puzzle. number + 1 must be perfect square]")
        if data and data.puzzle:
            solve(data)
    else:
        print ("usage: main.py [path to puzzle] OR [number for size of puzzle. "
               "number + 1 must be perfect square]")


if __name__ == '__main__':
    main()
