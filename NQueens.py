def isSafe(board, row, col):
	if 'Q' in board[row]:
		return False
	i=0
	j=0
	while i!=len(board):
		if board[i][col] == 'Q':
			return False
		i+=1
		j+=1

	i,j=0,0
	while i!=len(board):
		if row+i<len(board) and col+i < len(board):
			if board[row+i][col+j] == 'Q':
				return False

		if row-i>=0 and col-i >= 0:
			if board[row-i][col-j] == 'Q':
				return False

		if row+i<len(board) and col-j >= 0:
			if board[row+i][col-j] == 'Q':
				return False

		if row-i >= 0 and col+j < len(board):
			if board[row-i][col+j] == 'Q':
				return False
		i+=1
		j+=1

	return True




def solveNQueens(n):
	solution = []
	board = solveNQ()
	
	if board:
		solution.append(board)


