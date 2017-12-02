def board_to_string(board):
	array = []
	ma = len(board) - 1
	mi = 0
	x = 0
	y = 0
	array.append(board[x][y])
	while ma >= mi:
			while x < ma:
				x += 1
				array.append(board[y][x])
			while y < ma:
				y += 1
				array.append(board[y][x])
			while x > mi:
				x -= 1
				array.append(board[y][x])
			mi += 1
			ma -= 1
			while y > mi:
				y -= 1
				array.append(board[y][x])
	array.remove(0)
	return array