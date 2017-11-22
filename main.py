#!/usr/bin/env python3


from classes import *
import sys
from shift import *
from solve import solve

def main():
    if len(sys.argv) == 2:
        try:
            fd = open(sys.argv[1], 'r')
            data = Data(fd=fd)
            fd.close()
        except OSError:
            if sys.argv[1].isdigit():
                data = Data(sys.argv[1])
                print ("puzzle size = " + str(data.size) + " Puzzle = " + str(data.puzzle))
            else:
                print ( "usage: main.py [path to puzzle] OR [number for size of "
                        "puzzle. number + 1 must be perfect square]")
        if data.puzzle:
            solve(data)
    else:
        print ("usage: main.py [path to puzzle] OR [number for size of puzzle. number + 1 must be perfect square]")



if __name__ == '__main__':
    main()
