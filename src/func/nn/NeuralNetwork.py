#/**
# * An abstract class representing a network
# * @author Andrew Guillory gtg008g@mail.gatech.edu
# * @version 1.0
# */
class NeuralNetwork:
   
#    /**
#     * Get link values
#     * @return the link values
#     */
   def getWeights(self):
        links = getLinks()
        weights = double[links.size()]
        for i in range(len(weights)):
            l = links.get(i)
            weights[i] = l.getWeight()
        return weights
    
#    /**
#     * Set link values
#     * @param weights the link values
#     */
# This seems like it should be links...as in set links... don't know
   def setWeights(self, weights):
        links = getLinks();
        for i in range(len(weights)):
            l = links.get(i)
            l.setWeight(weights[i])
#    /**
#     * Set the weights of a neural network
#     * @param weights the weight vector
#     */
   def setWeights(self, weights):
        links = getLinks();
        for i in range(len(weights)):
            l = links.get(i)
            l.setWeight(weights.get(i))
