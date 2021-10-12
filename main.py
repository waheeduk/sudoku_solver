#ten lists to represent the values in a sudoku puzzle
grid =[
[2, 0, 6, 3, 7, 0, 0, 0, 0 ],
[5, 1, 0, 4, 0, 0, 7, 0, 0 ],
[4, 3, 0, 0, 6, 0, 0, 0, 8 ],
[9, 6, 0, 0, 5, 0, 0, 0, 0 ],
[0, 5, 3, 0, 8, 0, 0, 0, 0 ],
[7, 8, 0, 0, 1, 0, 5, 4, 9 ],
[0, 4, 0, 0, 0, 0, 0, 5, 7 ],
[0, 7, 5, 0, 9, 6, 2, 0, 0 ],
[0, 0, 1, 7, 4, 0, 3, 9, 6 ]
]

def display():
	"""displays data of sudoku grid in a readable format"""
	for n in grid:
		print(n)

def possible(x, y, n, grid):
	"""takes value n and checks if its possible to input it at grid coordinate x, y"""
	#checks for duplicates along y axis
	for i in range(0, 9):
		if grid[y][i] == n:
			return False
	#checks for duplicates along x axis
	for i in range(0, 9):
		if grid[i][x] == n:
			return False
	#checks for duplicates in 3x3 grid quadrant
	qx = (x // 3) * 3
	qy = (y // 3) * 3
	for a in range(0, 3):
		for b in range(0, 3):
			if grid[qy + b][qx + a] == n:
				return False
	return True

def solve():
	"""recursively solves the sudoku grid"""
	for y in range(0, 9):
		for x in range(0, 9):
			if grid[y][x] == 0:
				for n in range(1, 10):
					if possible(x, y, n, grid):
						grid[y][x] = n
						solve()
						grid[y][x] = 0
				return 
	for x in range(0, 9):
		print(grid[x])

solve()
