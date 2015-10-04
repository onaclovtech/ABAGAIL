#/**
# * @author kmanda1
# */

class NQueensFitnessFunction (EvaluationFunction):

#	/**
#	 * the number of moves the above algorithm takes to 
#	 * find the first solution
#	 */
	def value(self, Instance d):
		fitness = 0

		board = self.getBoardForGivenInstance(d)
		currentBoard = board
		boardSize = board.getSize()

		// Calculate the number of non-attacking pairs of queens 
		qPositions = board.getQueenPositions()
		
		for (fromX = 0; fromX < (boardSize - 1); fromX++):
			for (toX = fromX + 1; toX < boardSize; toX++):
				fromY = qPositions.get(fromX).getYCoOrdinate()
				nonAttackingPair = true
				// Check right beside
				toY = fromY
				if (board.queenExistsAt(new BoardLocation(toX, toY))):
					nonAttackingPair = false
				// Check right and above
				toY = fromY - (toX - fromX)
				if (toY >= 0):
					if (board.queenExistsAt(new BoardLocation(toX, toY))):
						nonAttackingPair = false
				// Check right and below
				toY = fromY + (toX - fromX)
				if (toY < boardSize):
					if (board.queenExistsAt(new BoardLocation(toX, toY))):
						nonAttackingPair = false

				if (nonAttackingPair):
					fitness += 1.0
		return fitness;

#	/**
#	 * 
#	 * @param d
#	 * @return
#	 */
	def getBoardForGivenInstance(self, Instance d):
		boardSize = d.size()
		board = new NQueensBoardGame(boardSize)
		for (i = 0; i < boardSize; i++):
			pos = d.getDiscrete(i)
			board.addQueenAt(new BoardLocation(i, pos))
		return board

	def boardPositions(self):
		return self.currentBoard
