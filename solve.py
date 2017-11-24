from node import Node
from shift import print_list


def solve(data):
    start = Node(data.puzzle)
    print("Start")
    print_list(start.data)
    end = data.goal
    print('End')
    print_list(end)
    h = start.man_h(end)
    print("h = ", h)
    open = []
    closed = []
    open = start.expand()
    # for N in open:
    #     print(N.h)
    #     N.man_h(N.data)
    #     print(N.h)
