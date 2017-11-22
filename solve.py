from shift import *


def list_nodes(grid):
    nodes = []
    tmp = right_shift(grid)
    if tmp:
        nodes.append(tmp)
    tmp = left_shift(grid)
    if tmp:
        nodes.append(tmp)
    tmp = up_shift(grid)
    if tmp:
        nodes.append(tmp)
    tmp = down_shift(grid)
    if tmp:
        nodes.append(tmp)
    return nodes


def print_list(l):
    if l:
        for row in l:
            print (row)


def solve(data):
    test = data.puzzle

    print ("Original")
    print_list(test)
    print ('\n')
    l = list_nodes(test)
    for n in l:
        print_list(n)
        print ('\n')