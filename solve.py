from node import Node
from shift import print_list


class Open(object):

    def __init__(self, goal):
        self.nodes = []
        self.goal = goal
        self.current = 0
        self.max_held = 0
        self.total = 0

    def add(self, new):
        self.nodes.append(new)
        self.total += 1
        # sorts list so smalled h is last
        self.nodes.sort(key=lambda x: x.f, reverse=True)
        length = len(self.nodes)
        if self.max_held < length:
            self.max_held = length

    def lowest_f(self):
        if self.nodes:
            return self.nodes.pop()
        return None

    def get_node(self, grid):
        for node in self.nodes:
            if node.data == grid:
                return node
        return None


def path_to_solution(node):
    path = []
    cur = node
    while cur:
        path.append(cur)
        cur = cur.parent
    path.reverse()
    for e in path:
        print_list(e.data)


def a_star(data):
    start = Node(data.puzzle, None, data.goal)
    end = data.goal
    closed = []
    open = Open(end)
    open.add(start)
    while open.nodes:
        process = open.lowest_f()
        if process.data == end:
            print('total moves = ', process.g)
            return path_to_solution(process)
        closed.append(process.data)
        expanded = process.expand(end)
        for node in expanded:
            actual_node = open.get_node(node.data)
            if node.data not in closed and actual_node == None:
                open.add(node)
            elif actual_node:
                if node.g < actual_node.g:
                    actual_node.g = node.g
                    actual_node.f = node.f
                    actual_node.parent = node.parent
    print('No possible solution')

