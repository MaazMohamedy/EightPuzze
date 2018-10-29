

def main():
	puzzleType = input("Welcome to Maaz Mohamedy's 8-puzzle solver.\nType '1' to use default puzzle," +
		" or '2' to create your own. \n")

	if puzzleType == '1':
		puzzle = pickDefaultArrangement()

	if puzzleType == '2':
		pickCustomArrangement()

		
		
def pickCustomArrangement():
	puzzle = []
	print("Enter your puzzle, use a zero to represent the blank")
	row1 = input("Enter the first row, use space or tabs between numbers\n").split()
	row2 = input("Enter the second row, use space or tabs between numbers\n").split()
	row3 = input("Enter the third row, use space or tabs between numbers\n").split()
	
	for i in range(0, 3):
		row1[i] = int(row1[i])
		row2[i] = int(row2[i])
		row3[i] = int(row3[i])
	
	puzzle.append(row1)
	puzzle.append(row2)
	puzzle.append(row3)

	return puzzle


def pickDefaultArrangement():
	level = input("Which level of difficulty do you want? \nType '1' for Trivial, '2' for Very Easy," +
		" '3' for Easy, '4' for doable, '5' for Oh Boy, '6' for impossible. \n")
	#trivial
	if level == '1':
		trivial = [[1,2,3],
		[4,5,6],
		[7,8,0]]
		return trivial;
	#Very Easy
	if level == '2':
		trivial = [[1,2,3],
		[4,5,6],
		[7,0,8]]
		return trivial;
	#Easy
	if level == '3':
		trivial = [[1,2,0],
		[4,5,3],
		[7,8,6]]
		return trivial;
	#doable
	if level == '4':
		trivial = [[0,1,2],
		[4,5,3],
		[7,8,6]]
		return trivial;
	#Oh Boyy
	if level == '5':
		trivial = [[8,7,1],
		[6,0,2],
		[5,4,3]]
		return trivial;
	#IMPOSSIBLE
	if level == '6':
		trivial = [[1,2,3],
		[4,5,6],
		[8,7,0]]
		return trivial;



if __name__ == "__main__":
	main()