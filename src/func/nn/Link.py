#/**
# * A link between two nodes in a neural network
# * @author Andrew Guillory gtg008g@mail.gatech.edu
# * @version 1.0
# */
def Link(Serializable):
    
    /**
     * Create a new linke
     * initializes the weight to a random value
     */
    def __init__():
        self.random = new Random() # Update
	self.inNode
	self.outNode
        self.weight = self.random.nextDouble() * 2 - 1
        
#	/**
#	 * Get the in node
#	 * @return the node
#	 */
	def getInNode(self):
		return self.inNode
    
#    /**
#     * Set the in node
#     * @param node the node
#     */
    def setInNode(self, node):
        self.inNode = node

#	/**
#	 * Get the out node
#	 * @return the node
#	 */
    def getOutNode(self):
	return self.outNode
    
#    /**
#     * Set the out node
#     * @param node the node
#     */
    def setOutNode(Neuron node):
        self.outNode = node
	
#	/**
#	 * Get the input value
#	 * @return the value
#	 */
	def getInValue(self):
		return self.inNode.getActivation()
	
#	/**
#	 * Get the output value
#	 * @return the value
#	 */
	def getOutValue(self):
		return self.outNode.getActivation()
	
#	/**
#	 * Get the weighted out value
#	 * @return the weighted out value
#	 */
	def getWeightedOutValue(self):
		return self.outNode.getActivation() * weight
	
#	/**
#	 * Get the weighted in value
#	 * @return the value
#	 */
	def getWeightedInValue(self):
		return self.inNode.getActivation() * weight

#	/**
#	 * Get the weight of the link
#	 * @return the weight
#	 */
	def getWeight():
		return self.weight

#	/**
#	 * Set the weight of the link
#	 * @param d the new weight
#	 */
	def setWeight(self, d):
		self.weight = d

#	/**
#	 * Update the weight
#	 * @param delta the change in weight
#	 */
	def changeWeight(self, delta):
		self.weight += delta
