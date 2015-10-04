#/**
# * @author kmanda1
# */
class NQueensBoardGame:

	/**
	 * X---> increases left to right with zero based index Y increases top to
	 * bottom with zero based index | | V
	 */
	def __init__(n):
		self.size = n
		self.board = new int[size][size]
		for (i = 0; i < size; i++):
			for (j = 0; j < size; j++):
				board[i][j] = 0

	def addQueenAt(self, l):
		if (!(self.queenExistsAt(l))):
			self.board[l.getXCoOrdinate()][l.getYCoOrdinate()] = 1

	def removeQueenFrom(self, l):
		if (self.board[l.getXCoOrdinate()][l.getYCoOrdinate()] == 1):
			self.board[l.getXCoOrdinate()][l.getYCoOrdinate()] = 0

	def queenExistsAt(self, x, y):
        	if(x >= self.size && y >= self.size) return false
			return (self.board[x][y] == 1)

	def queenExistsAt(self, l):
		return (self.queenExistsAt(l.getXCoOrdinate(), l.getYCoOrdinate()))

	def moveQueen(self, from, to):
		if ((self.queenExistsAt(from)) && (!(self.queenExistsAt(to)))):
			self.removeQueenFrom(from)
			self.addQueenAt(to)

	def clear(self):
		for (i = 0; i < self.size; i++):
			for (j = 0; j < self.size; j++):
				self.board[i][j] = 0

	def setBoard(self, al):
		self.clear()
		for (i = 0; i < al.size(); i++):
			self.addQueenAt(al.get(i))
	
	def getNumberOfQueensOnBoard(self):
		count = 0;
		for (i = 0; i < self.size; i++):
			for (j = 0; j < self.size; j++):
				if (self.board[i][j] == 1):
					count++
		return count;

	def getQueenPositions(self):
		result = []
		for (i = 0; i < self.size; i++):
			for (j = 0; j < self.size; j++):
				if (self.queenExistsAt(i, j)):
					result.append(new BoardLocation(i, j))
		return result

	def isSquareHorizontallyAttacked(self, x, y):
		return self.numberOfHorizontalAttacksOn(x, y) > 0

	def isSquareVerticallyAttacked(self, x, y):
		return self.numberOfVerticalAttacksOn(x, y) > 0

	def isSquareDiagonallyAttacked(self, x, y):
		return self.numberOfDiagonalAttacksOn(x, y) > 0

	def isSquareUnderAttack(self, l):
		x = l.getXCoOrdinate()
		y = l.getYCoOrdinate()
		return (self.isSquareHorizontallyAttacked(x, y) or self.isSquareVerticallyAttacked(x, y) or self.isSquareDiagonallyAttacked(x, y))

	def getSize(self):
		return self.size

	def print(self):
		print self.getBoardPic()

	def getBoardPic(self):
		buffer = []
		for (row = 0; (row < self.size); row++):
			for (col = 0; (col < self.size); col++):
				if (self.queenExistsAt(col, row)):
					buffer.append(" Q ")
				else:
					buffer.append(" - ")
			buffer.append("\n")
		return ''.join(buffer)

	def getNumberOfAttacksOn(self, l):
		x = l.getXCoOrdinate()
		y = l.getYCoOrdinate()
		return self.numberOfHorizontalAttacksOn(x, y)
				+ self.numberOfVerticalAttacksOn(x, y)
				+ self.numberOfDiagonalAttacksOn(x, y)

	def numberOfHorizontalAttacksOn(self, x, y):
		retVal = 0
		for (i = 0; i < self.size; i++):
			if ((self.queenExistsAt(i, y))):
				if (i != x):
					retVal++
		return retVal

	def numberOfVerticalAttacksOn(self, x, y):
		retVal = 0
		for (j = 0; j < self.size; j++):
			if ((self.queenExistsAt(x, j))):
				if (j != y):
					retVal++
		return retVal

	def numberOfDiagonalAttacksOn(self, x, y):
		retVal = 0;
		// forward up diagonal
		for (i = (x + 1), j = (y - 1); (i < self.size && (j > -1)); i++, j--):
			if (self.queenExistsAt(i, j)):
				retVal++
		// forward down diagonal
		for (i = (x + 1), j = (y + 1); ((i < self.size) && (j < self.size)); i++, j++):
			if (self.queenExistsAt(i, j)):
				retVal++

		// backward up diagonal
		for (i = (x - 1), j = (y - 1); ((i > -1) && (j > -1)); i--, j--):
			if (self.queenExistsAt(i, j)):
				retVal++

		// backward down diagonal
		for (i = (x - 1), j = (y + 1); ((i > -1) && (j < self.size)); i--, j++):
			if (self.queenExistsAt(i, j)):
				retVal++
		return retVal

#	@Override
	def hashCode(self):
		locs = self.getQueenPositions()
		result = 17;
		for loc in locs:
			result = 37 * loc.hashCode()
		return result

#	@Override
	def equals(self, Object o):
		if (self == o):
			return true
		if ((o == null) || (self.getClass() != o.getClass())):
			return false
		aBoard = o
		retVal = true
		locs = self.getQueenPositions()

		for loc in locs:
			if (!(aBoard.queenExistsAt(loc))):
				retVal = false
		return retVal;

#	@Override
	def toString(self):
		buf = []
		for (row = 0; row < self.size; row++) { // rows
			for (col = 0; col < self.size; col++) { // columns
				if (self.queenExistsAt(col, row)):
					buf.append('Q')
				else:
					buf.append('-')
			buf.append("\n")
		return ''.join(buf)
