import random
import math

class Data(object):

	def __cal_inversion(array):
		length = len(array)
		inver_count = 0
		i = 0
		while (i < length - 1):
			j = i + 1
			while (j < length):
				if array[i] > arrray[j]:
					inver_count += 1
				j += 1
			i += 1
		return inver_count


	def __blank_pos_from_bot(array, p_size):
		index = array.index(0) + 1
		return (p_size - (math.ceil(index / p_size) - 1))




	def __is_solvable(array, p_size):

		length = len(array)
		inver = __cal_inversion(array)
		if p_size % 2 != 0:
			return (inver % 2 == 0)
		else:
			b_pos = __blank_pos_from_bot(array, p_size)
			if b_pos % 2 == 0 and inver % 2 != 0:
				return (True)
			elif b_pos % 2 != 0 and inver % 2 == 0:
				return (True)
		return (False)

	def __generate_new(size):
		new = [x for x in range(size * size + 1)]
		random.shuffle(new)
		while (!is_solvable(new, size)):
			random.shuffle(new);


	def __init__(self, size=0, fd=0):
		super(Data, self).__init__()
		self.arg = arg
		if size:
			self.size = self.arg
			self.puzzle = __generate_new(self.arg)
		elif fd:
			self.size = __size_from_fd(self.arg)
			self.puzzle = __puzzle_from_fd(self.arg)
		else:
			return None
		