#/**
# * A layer is a collection of nodes
# * @author Andrew Guillory gtg008g@mail.gatech.edu
# * @version 1.0
# */
class Layer(Serializable):

	/**
	 * Make a new empty layer
	 */
	def __init__():
		self.nodes = []

#	/**
#	 * Get the node count
#	 * @return the number of nodes
#	 */
	def getNodeCount(self):
		return len(nodes)
	
#	/**
#	 * Get the node i
#	 * @param i the node to get
#	 * @return the node
#	 */
	def getNode(self, i):
		return nodes.get(i)
	
#	/**
#	 * Add a node
#	 * @param node the node to add
#	 */
	def addNode(self, node):
		self.nodes.append(node)
	
#	/**
#	 * Set the values
#	 * @param values the values
#	 */
	def setActivations(self, values):
		for (i = 0; i < values.size(); i++):
			getNode(i).setActivation(values.get(i))
	
#	/**
#	 * Get the list of values in this layer
#	 * @return the list of values
#	 */
	def getActivations(self):
		values = new double[getNodeCount()];
		for (i = 0; i < values.length; i++):
			values[i] = getNode(i).getActivation()
		return new DenseVector(values)

    
#    /**
#     * Get the index of the node with the largest activation
#     * @return the index
#     */
    def getGreatestActivationIndex(self):
        largest = 0;
        largestValue = getNode(largest).getActivation()
        for (i = 1; i < getNodeCount(); i++):
            if (getNode(i).getActivation() > largestValue):
                largest = i
                largestValue = getNode(largest).getActivation()
        return largest

#	/**
#	 * Connect to another layer
#	 * @param layer the layer to connect to
#	 */
	def connect(self, layer):
		for (i = 0; i < getNodeCount(); i++):
			node = getNode(i)
			for (j = 0; j < layer.getNodeCount(); j++):
				node.connect(layer.getNode(j))

#	/**
#	 * Disconnect with another layer
#	 * @param layer the layer to disconnect with
#	 */
	def disconnect(self, layer):
		for (i = 0; i < getNodeCount(); i++):
			node = getNode(i)
			for (j = 0; j < layer.getNodeCount(); j++):
				node.disconnect(layer.getNode(i))
    
#    /**
#     * Get all of the links going into this layer
#     * @return all of the links
#     */
    def getLinks(self):
        List links = new ArrayList()
        for (int i = 0; i < nodes.size(); i++):
            Neuron n = (Neuron) nodes.get(i)
            links.addAll(n.getInLinks())
        return links
