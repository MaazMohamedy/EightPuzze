import heapq

def main():
	puzzleType = input("Welcome to Maaz Mohamedy's 8-puzzle solver.\nType '1' to use default puzzle," +
		" or '2' to create your own. \n")

	if puzzleType == '1':
		puzzle = pickDefaultArrangement()

	if puzzleType == '2':
		puzzle = pickCustomArrangement()

	# print(puzzle)

	algo = input("Enter your choice of algorithm"  +
		"\n\t1. Uniform Cost Search"
		"\n\t2. A* with the Misplaced Tile heuristic." +
		"\n\t3. A* with the Manhattan distance heuristic.\n")

	generalSearch(puzzle,algo)

def misplacedTileHeuristic(puzzle):
	numMisplaced = 0;
	val = 1
	for i in range(0,len(puzzle)):
		for j in range(0,len(puzzle[i])):
			if val == 9: val = 0
			if puzzle[i][j] != val and puzzle[i][j] != 0:
				numMisplaced = numMisplaced + 1
			val = val + 1

	return numMisplaced

def manhattanDistanceHeuristic(puzzle):
	val = 1
	manhattanSum = 0
	for i in range(0,len(puzzle)):
		for j in range(0,len(puzzle[i])):
			if val == 9: val = 0
			if puzzle[i][j] != val and puzzle[i][j] != 0:
				x,y = findIndicesOfGoalState(puzzle[i][j])
				horizontal = abs(j - x)
				vertical = abs(i - y)
				moves  = horizontal + vertical
				manhattanSum = manhattanSum + moves
			val = val + 1

	return manhattanSum

def findIndicesOfGoalState(val):
	goal = [[1,2,3], [4,5,6], [7,8,0]]
	for i in range(0,len(goal)):
		for j in range(0,len(goal[i])):
			if goal[i][j] == val:  return(j,i)

def calculateHeuristic(algo, puzzle):
	if algo == "1": return 0
	if algo == "2":
		return misplacedTileHeuristic(puzzle)
	if algo == "3":
		return manhattanDistanceHeuristic(puzzle)

def expand(node, algo):
	children = []
	currPuzzle = node[1]

	i,j = 0,0
	x,y = 0,0
	#find blank position of blank space
	for i in range(0, len(node[1])):
		for j in range(0, len(node[1][i]) ):
			if node[1][i][j] == 0:
				x,y = i,j
				break

	
	if x+1 < (len(node[1])):
		# shift blank space down
		shiftDown = list(map(list, node[1],))	
		shiftDown[x][y], shiftDown[x+1][y] = shiftDown[x+1][y] , shiftDown[x][y]
		# calculate hn and gn
		hOfN = calculateHeuristic(algo, shiftDown)
		gOfN = node[2] + 1
		updatedCost = gOfN + hOfN
		children.append((updatedCost,shiftDown,gOfN,hOfN))

	if y-1 >= 0:
		# shift blank space left
		shiftLeft = list(map(list, node[1],))	
		shiftLeft[x][y], shiftLeft[x][y-1] = shiftLeft[x][y-1] , shiftLeft[x][y]
		# calculate hn and gn
		hOfN = calculateHeuristic(algo, shiftLeft)
		gOfN = node[2] + 1
		updatedCost = gOfN + hOfN
		children.append((updatedCost,shiftLeft,gOfN,hOfN))

	if x-1 >= 0:
		# shift blank space up
		shiftUp = list(map(list, node[1],))	
		shiftUp[x][y], shiftUp[x-1][y] = shiftUp[x-1][y] , shiftUp[x][y]
		# calculate hn and gn
		hOfN = calculateHeuristic(algo, shiftUp)
		gOfN = node[2] + 1
		updatedCost = gOfN + hOfN
		children.append((updatedCost,shiftUp,gOfN,hOfN))


	if y+1 < (len(node[1])):
		# shift blank space right
		shiftRight = list(map(list, node[1],))	
		shiftRight[x][y], shiftRight[x][y+1] = shiftRight[x][y+1] , shiftRight[x][y]
		# calculate hn and gn
		hOfN = calculateHeuristic(algo, shiftRight)
		gOfN = node[2] + 1
		updatedCost = gOfN + hOfN
		children.append((updatedCost,shiftRight,gOfN,hOfN))

	return children

def generalSearch(puzzle, algo):
	#4^(d+1) - 5
	goalState = [[1,2,3],[4,5,6],[7,8,0]]
	failure = False;
	maxQueueLen = 0;
	nodes = []

	first = ''
	for i in range(0,len(puzzle[0])):
		if  puzzle[0][i] != 0:  first=first+' '+str(puzzle[0][i])
		else: first=first+' '+'b'

	print("Expanding state " + first, end =" ")
	printExpansion(puzzle[1:], True, 0, 0)

	first_expansion = True

	#total cost, puzzle, depth, h(n)
	heapq.heappush(nodes, (0, puzzle, 0,0) )

	while(True):
		if len(nodes) == 0: #if nodes is empty, return failure
			print("FAILURE")
			return currNode

		if maxQueueLen < len(nodes): maxQueueLen = len(nodes)
		currNode = heapq.heappop(nodes)

		if not first_expansion:
			printExpansion(currNode[1],False,currNode[3], currNode[2])

		first_expansion = False

		if currNode[1] == goalState:
			print("Goal!! \n")
			print("The maximum number of nodes in the queue at any one time was " + str(maxQueueLen))
			print("The depth of the goal node was " + str(currNode[2]))
			return currNode;

		children = expand(currNode, algo)

		for child in children:
			heapq.heappush(nodes, child)

	return

def printExpansion(puzzle,first,hOfN, gOfN):
	print()
	row = ''
	if not first:
		print('The best state to expand with a g(n) = ' + str(gOfN)+ ' and h(n) = ' + str(hOfN) + ' is...')
	for i in range(0,len(puzzle)):
		for j in range(0,len(puzzle[i])):
			if  puzzle[i][j] != 0:  row = row + ' '+ str(puzzle[i][j])
			else: row=row+' '+'b'
		row = '\t\t' + row
		if first == False and i == 2: row = row + ' Expanding this node...'
		print(row)
		row = ''

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
		veryEasy = [[1,2,3],
		[4,5,6],
		[7,0,8]]
		return veryEasy;
	#Easy
	if level == '3':
		easy = [[1,2,0],
		[4,5,3],
		[7,8,6]]
		return easy;
	#doable
	if level == '4':
		doable = [[0,1,2],
		[4,5,3],
		[7,8,6]]
		return doable;
	#Oh Boyy
	if level == '5':
		ohBoy = [[8,7,1],
		[6,0,2],
		[5,4,3]]
		return ohBoy;
	#IMPOSSIBLE
	if level == '6':
		impossible = [[1,2,3],
		[4,5,6],
		[8,7,0]]
		return impossible;

if __name__ == "__main__":
	main()