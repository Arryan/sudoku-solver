initial_board = [
	[ 0, 0, 0,  0, 0, 0,  0, 0, 0 ],
	[ 0, 0, 0,  0, 0, 3,  0, 8, 5 ],
	[ 0, 0, 1,  0, 2, 0,  0, 0, 0 ],

	[ 0, 0, 0,  5, 0, 7,  0, 0, 0 ],
	[ 0, 0, 4,  0, 0, 0,  1, 0, 0 ],
	[ 0, 9, 0,  0, 0, 0,  0, 0, 0 ],

	[ 5, 0, 0,  0, 0, 0,  0, 7, 3 ],
	[ 0, 0, 2,  0, 1, 0,  0, 0, 0 ],
	[ 0, 0, 0,  0, 4, 0,  0, 0, 9 ] 
] 

##########################################
def valid_cell(row, col, b):
	value = b[row][col]
	count = 0;

	for i in range(9):
		#check row
		if b[row][i] == value:
			count += 1
		
		#check column
		if b[i][col] == value:
			count += 1
		
		if count > 2:
			return False;
	
	#check box
	count = 0
	for i in range(row - (row % 3), row - (row % 3) + 3):
		for j in range(col - (col % 3), col - (col % 3) + 3):
		  print(str(i) +  str(j) + " " + str(b[i][j]))
		  if b[i][j] == value:
		    if count == 1:
		      return False
		    count += 1
		  
	return True

##########################################
def valid_board(b):
	valid = True
	for row in range(9):
		for col in range(9):
			if b[row][col] != 0 and not valid_cell(row, col, b):
				valid = False
	return valid

##########################################
def solve_board(b):
	

##########################################
def print_board(b):
	for row in range(9):
		for row in range(9):
			if b[row][col] == 0:
				print(".", end=" ")
			else:
				print(b[row][col], end=" ")
			if x == 2 or x == 5:
				print("|", end=" ")
			else:
				print(" ", end=" ")
		print()

print_board(initial_board)
