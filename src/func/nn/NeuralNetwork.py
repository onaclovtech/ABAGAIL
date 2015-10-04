#/**
# * An abstract class representing a network
# * @author Andrew Guillory gtg008g@mail.gatech.edu
# * @version 1.0
# */
class NeuralNetwork(Serializable):
	
#	/**
#	 * Get the output values
#	 * @return the output values
#	 */
	def getOutputValues():
		print ""	
#	/**
#	 * Set intput values
#	 * @param values the new values
#	 */
	def setInputValues(self, values):
		print ""    
#    /**
#     * Run the network on the input values and
#     * generate the output values.
#     */
    def run():
    	print ""
    
#    /**
#     * Get all of the weights in the neural network
#     * @return all of the weights in the network
#     */
    def getLinks():
    	print ""
    
#    /**
#     * Get link values
#     * @return the link values
#     */
    def getWeights(self):
        links = getLinks()
        weights = new double[links.size()]
        for (i = 0; i < weights.length; i++):
            Link l = (Link) links.get(i)
            weights[i] = l.getWeight()
        return weights
    
#    /**
#     * Set link values
#     * @param weights the link values
#     */
    def setWeights(self, weights):
        links = getLinks();
        for (i = 0; i < weights.length; i++):
            l = (Link) links.get(i)
            l.setWeight(weights[i])
#    /**
#     * Set the weights of a neural network
#     * @param weights the weight vector
#     */
    def setWeights(self, weights):
        links = getLinks();
        for (i = 0; i < weights.size(); i++):
            l = (Link) links.get(i)
            l.setWeight(weights.get(i))
