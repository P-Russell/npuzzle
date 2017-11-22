from create import is_solvable

def flatten_array(l):
    flat = []
    for row in l:
        for e in row:
            flat.append(e)
    return flat

def valid_data(size, grid):
    found = []
    elements = size * size - 1
    if size != len(grid):
        print ("Puzzle in conflict with stated size")
        return False
    for row in grid:
        if len(row) != size:
            print ("invalid row length")
            return False
        for e in row:
            if e not in found:
                found.append(e)
            else:
                print ("Duplicate elements in puzzle")
                return False
            if not e.isdigit() or int(e) > elements:
                print ("Invalid element: " + e)
                return False
    if not is_solvable(flatten_array(grid), size):
        print ("puzzle not solvable")
        return False
    return True


def data_in_line(s):
    if not s or not s.partition('#')[0]:
        return False
    return True


def puzzle_from_fd(fd):
    grid = []
    line = fd.readline().strip()
    while not data_in_line(line):
        line = fd.readline().strip()
    if line.partition('#')[0].isdigit():
        size = int(line)
    else:
        print ("First line of file " + fd.name + " needs to be puzzle size")
        return None, None
    line = fd.readline()
    while line:
        if data_in_line(line):
            line = line.partition('#')[0].rstrip()
            grid.append(line.split())
        line = fd.readline()
    if valid_data(size, grid):
        return size, grid
    return None, None