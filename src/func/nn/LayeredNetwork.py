#/**
# * A layered neural network
# * @author Andrew Guillory gtg008g@mail.gatech.edu
# * @version 1.0
# */
class LayeredNetwork(NeuralNetwork):



	
#	/**
#	 * Make a new layered network
#	 */
	def __init__():
		self.hiddenLayers = [];
		self.inputLayer = new Layer()
		self.outputLayer = new Later()
		self.links = null;

#	/**	
# 	 * @see Network#getOutputValues()
# 	 */
	def getOutputValues(self):
		return self.outputLayer.getActivations()
	
#	/**
#	 * @see Network#setInputValues(double[])
#	 */
	def setInputValues(self, Vector values):
		self.inputLayer.setActivations(values)
    
#    /**
#     * Get the index of the node with the largest value
#     * @return the index
#     */
	def getDiscreteOutputValue(self):
        	return self.outputLayer.getGreatestActivationIndex()
    
#    /**
#     * Get the binary output value
#     * @return the binary output value
#     */
    def getBinaryOutputValue(self):
        return self.outputLayer.getNode(0).getActivation() > .5

#	/**
#	 * Get the input layer
#	 * @return the layer
#	 */
	def getInputLayer(self):
		return inputLayer

#	/**
#	 * Get the list of middle layers
#	 * @return the list
#	 */
	def getHiddenLayers(self):
		return hiddenLayers

#	/**
#	 * Get the output layer
#	 * @return the layer
#	 */
	def getOutputLayer(self):
		return outputLayer

#	/**
#	 * Set the input layer
#	 * @param layer the new layer
#	 */
	def setInputLayer(self, layer):
		inputLayer = layer

#	/**
#	 * Set the output layer
#	 * @param layer the output layer
#	 */
	def setOutputLayer(self, layer):
		outputLayer = layer

#	/**
#	 * Get the middle layer count
#	 * @return the middle layer count
#	 */
	def getHiddenLayerCount(self):
		return len(self.hiddenLayers)
	
#	/**
#	 * Get the middle layer
#	 * @param i the index of the middle layer
#	 * @return the layer
#	 */
	def getHiddenLayer(self, int i):
		return self.hiddenLayers.get(i) # Returns a layer, dunno
	
#	/**
#	 * Add a middle layer
#	 * @param layer the layer to add
#	 */
	def addHiddenLayer(self, layer):
		self.hiddenLayers.add(hiddenLayers.size(), layer)

#	/**
#	 * Disconnect this network
#	 */
	def disconnect(self) {
		if (self.inputLayer != null && self.getHiddenLayerCount() > 0):
			Layer firstMiddle = self.getHiddenLayer(0)
			self.inputLayer.disconnect(firstMiddle)
		else:
			if (self.inputLayer != null && self.outputLayer != null):
				self.inputLayer.disconnect(self.outputLayer)
		for (i = 0; i + 1 < self.getHiddenLayerCount(); i++):
			Layer first = self.getHiddenLayer(i)
			Layer second = self.getHiddenLayer(i + 1)
			first.disconnect(second)
		if (self.outputLayer != null && self.getHiddenLayerCount() > 0):
			Layer lastMiddle = getHiddenLayer(getHiddenLayerCount() - 1)
			lastMiddle.disconnect(outputLayer)
#	/**
#	 * Connect this network
#	 */
	def connect(self) {
		if (self.inputLayer != null && self.getHiddenLayerCount() > 0):
			Layer firstMiddle = self.getHiddenLayer(0)
			self.inputLayer.connect(firstMiddle)
		else:
			if (self.inputLayer != null && self.outputLayer != null):
				self.inputLayer.connect(self.outputLayer)
		for (int i = 0; i + 1 < self.getHiddenLayerCount(); i++):
			Layer first = self.getHiddenLayer(i)
			Layer second = self.getHiddenLayer(i + 1)
			first.connect(second)
		if (self.outputLayer != null && self.getHiddenLayerCount() > 0):
			Layer lastMiddle = self.getHiddenLayer(self.getHiddenLayerCount() - 1)
			lastMiddle.connect(self.outputLayer)
#    /**
#     * @see nn.NeuralNetwork#getLinks()
#     */
    def getLinks(self):
       if (self.links != null):
           return self.links
       self.links.addAll(self.inputLayer.getLinks())
       for (int i = 0; i < self.getHiddenLayerCount(); i++):
           self.links.addAll(self.getHiddenLayer(i).getLinks())
       self.links.addAll(self.outputLayer.getLinks())
       return links
