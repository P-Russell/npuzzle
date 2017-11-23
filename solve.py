from shift import *


def expand_node(grid):
    nodes = []
    tmp = right_shift(grid)
    print ('Nodes created inside list_nodes')
    if tmp:
        print ('shift right')
        print_list(tmp)
        nodes.append(tmp)
    tmp = left_shift(grid)
    if tmp:
        print ('shift left')
        print_list(tmp)
        nodes.append(tmp)
    tmp = up_shift(grid)
    if tmp:
        print ('shift up')
        print_list(tmp)
        nodes.append(tmp)
    tmp = down_shift(grid)
    if tmp:
        print ('shift down')
        print_list(tmp)
        nodes.append(tmp)
    print('End of Nodes created inside of list_nodes')
    return nodes


def solve(data):
    test = data.puzzle
    size = data.size

    print ("Original")
    print_list(test)
    l = expand_node(test)