#/**
# * @author kmanda1
# */
class BoardLocation {
	def __init__(int i, int j):
		self.xCoOrdinate = i;
		self.yCoOrdinate = j;

	def getXCoOrdinate(self): 
		return self.xCoOrdinate

#	@Override
	def equals(self, Object o):
		BoardLocation anotherLoc = (BoardLocation) o
		return ((anotherLoc.getXCoOrdinate() == self.xCoOrdinate) && (anotherLoc.getYCoOrdinate() == self.yCoOrdinate))

	def getYCoOrdinate(self):
		return self.yCoOrdinate

	def west(self):
		return new BoardLocation(self.xCoOrdinate - 1, self.yCoOrdinate)

	def east(self):
		return new BoardLocation(self.xCoOrdinate + 1, self.yCoOrdinate)

	def north(self):
		return new BoardLocation(self.xCoOrdinate, self.yCoOrdinate - 1)

	def south(self):
		return new BoardLocation(self.xCoOrdinate, self.yCoOrdinate + 1)

	def right(self):
		return self.east()

	def left(self):
		return self.west()

	def up(self):
		return self.north()

	def down(self):
		return self.south()

	def locationAt(self, String direction):
		if (direction.equals("North")):
			return self.north()
		if (direction.equals("South")):
			return self.south()
		if (direction.equals("East")):
			return self.east()
		if (direction.equals("West")):
			return self.west()
		else:
			throw new RuntimeException("Unknown direction " + direction)

#	@Override
	def toString(self):
		return " ( " + self.xCoOrdinate + " , " + self.yCoOrdinate + " ) "

#	@Override
	def hashCode(self):
		int result = 17
		result = 37 * result + self.xCoOrdinate
		result = result + self.yCoOrdinate
		return result
