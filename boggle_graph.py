"""
Generate a graph of the boggle board
"""

def make_board(letters, board_dimensions):
	"""
	Returns a 2D matrix of the n x n board that is padded with None 
	and returns a dictionary of the positioning of the letters on the board 
	"""
	board = [[None for i in xrange(board_dimensions+2)] for i in xrange(board_dimensions+2)]
	position = {}
	x = 0
	y = 0
	for letter in letters:
		position[x, y] = letter.lower()
		y += 1
		if y >= board_dimensions:
			y = 0
			x += 1

	for (x, y) in position:
		board[x+1][y+1] = position[(x,y)]
	return board, position

def get_neighbors(board, current_position):
	"""
	Returns a list of the reachable neighbors of a certain node at position (x,y) on the board
	"""
	result = []
	x, y = current_position
	a, b = x-1, y-1
	neighbors = [(board[x-1][y-1], (a-1,b-1)), (board[x-1][y], (a-1,b)), \
				(board[x-1][y+1], (a-1, b+1)), (board[x][y-1], (a, b-1)), \
				(board[x][y+1], (a,b+1)), (board[x+1][y-1], (a+1, b-1)), \
				(board[x+1][y], (a+1, b)), (board[x+1][y+1], (a+1, b+1))]

	neighbors = [n for n in neighbors if n[0]]
	return neighbors

def make_graph(board, position):
	"""
	Returns a dictionary with the nodes as the keys and the reachable neighbors
	as the values
	"""
	graph = {}
	for node in position:
		graph[(position[node], node)] = get_neighbors(board, (node[0]+1, node[1]+1))
	graph[('', (None, None))] = [(position[node], node) for node in position]  # wildcard node - can start at any point on board
	return graph	

