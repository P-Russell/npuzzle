from node import Node
from shift import print_list


def solve(data):
    start = Node(data.puzzle)
    end = data.goal
    open = []
    closed = []

    open = start.expand()
    for N in open:
        print_list(N.data)
