import math
from find_item import *
from Board_to_String import *
from create_new import * 

def sh(a, size):
	temp = []
	grid = []
	i = 0
	for e in a:
		if i < size:
			temp.append(e)
		i += 1
		if i == size:
			grid.append(temp)
			temp = []
			i = 0
	return grid



def is_solvable(array, p_size):
	#print (array) 
	board = sh(array,p_size)
	#print (board)
	inversions = 0
	offset = 1
	for number in board:
#		print (number)
		index = 0 
		while index + offset < len(board):
			print (index + offset)
			if board[index + offset] < number:
				inversions += 1
				index += 1
			offset += 1
			if len(board) % 2 == 0:
				if find_item(string_to_board(board, len(board)), 0)[0][0] % 2 == 0 and inversions % 2 != 0:
					return True
				elif find_item(string_to_board(board, len(board)), 0)[0][0] % 2 != 0 and inversions % 2 == 0:
					return True
				else:
					return False
			else:
				if inversions % 2 == 0:
					return True
			#offset += 1	
		print ("poes")	

	#return False 


def blank_pos_from_bot(array, p_size):
	if 0 in array:
		index = array.index(0) + 1
	return p_size - (math.ceil(index / p_size) - 1)


def inversion(array):
	length = len(array)
	inv_count = 0
	i = 0
	while i < length - 1:
		j = i + 1
		while j < length:
			if array[i] > array[j]:
				inv_count += 1
			j += 1
		i += 1
	return inv_count
