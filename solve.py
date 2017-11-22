from shift import *


def list_nodes(grid):
    nodes = []
    tmp = right_shift(grid)
    print ('Nodes created inside of list_nodes')
    print ('initial grid id = ' + str(id(grid)))
    if tmp:
        print (id(tmp))
        print_list(tmp)
        nodes.append(tmp)
    tmp = left_shift(grid)
    if tmp:
        print (id(tmp))
        print_list(tmp)
        nodes.append(tmp)
    tmp = up_shift(grid)
    if tmp:
        print (id(tmp))
        print_list(tmp)
        nodes.append(tmp)
    tmp = down_shift(grid)
    if tmp:
        print (id(tmp))
        print_list(tmp)
        nodes.append(tmp)
    print('End of Nodes created inside of list_nodes')
    return nodes


def print_list(l):
    if l:
        print ('------------------------------')
        for row in l:
            print (row)
        print ('------------------------------')


def solve(data):
    test = data.puzzle

    print ("Original")
    print_list(test)
    l = list_nodes(test)
    for n in l:
        print_list(n)