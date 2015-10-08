from src.func.nn.Link import *
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
        links = self.getLinks()
        weights = [None] * len(links)
        for i in range(weights()):
            l = links[i]
            weights[i] = l.getWeight()
        return weights
    
#    /**
#     * Set link values
#     * @param weights the link values
#     */
# Here we can have an array of doubles or a Vector, well I'm not sure if we really need to differentiate, so I'm going to leave this as is
# for now
   def setWeights(self, weights):
        links = self.getLinks()
        for i in range(weights.size()):
            l = Link(links[i])
            l.setWeight(weights.get(i))
            
# #    /**
# #     * Set the weights of a neural network
# #     * @param weights the weight vector
# #     */
   # def setWeights(self, weights):
        # links = self.getLinks();
        # for i in range(len(weights)):
            # l = links[i]
            # l.setWeight(weights[i])
