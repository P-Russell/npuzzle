from is_solvable import is_solvable


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
			if e > elements:
				print ("Invalid element: " + str(e))
				return False
	if not is_solvable(flatten_array(grid), size):
		print ("puzzle not solvable")
		return False
	return True


def data_in_line(s):
	if not s or not s.partition('#')[0]:
		return False
	return True


def int_array(char_array):
	output = []
	for row in char_array:
		output.append([int(x) for x in row])
	return output


def puzzle_from_fd(fd):
	grid = []
	line = fd.readline().strip()
	while not data_in_line(line):
		line = fd.readline().strip()
	if line.partition('#')[0].isdigit():
		size = int(line)
	else:
		print ("First non-comment line of file " + fd.name + " needs to be puzzle size")
		return None, None
	line = fd.readline()
	while line:
		if data_in_line(line):
			line = line.partition('#')[0].strip()
			grid.append(line.split())
		line = fd.readline()
	grid = int_array(grid)
	if valid_data(size, grid):
		return size, grid
	return None, None
