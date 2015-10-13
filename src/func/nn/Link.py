import random
from src.func.nn.Neuron import *
#/**
# * A link between two nodes in a neural network
# * @author Andrew Guillory gtg008g@mail.gatech.edu
# * @version 1.0
# */
class Link:
    
    # /**
     # * Create a linke
     # * initializes the weight to a random value
     # */
   def __init__(self, inNode = Neuron(), outNode = Neuron(), weight = 0.0):
      #self.random =  #Random() # Update
      #random.nextDouble() * 2 - 1
      self.inNode = inNode
      self.outNode = outNode
      self.weight = random.random() * 2 - 1 #self.random.nextDouble() * 2 - 1
      #print "link.random_weight: "  + str(self.weight)
#   /**
#    * Get the in node
#    * @return the node
#    */
   def getInNode(self):
      return self.inNode
    
#    /**
#     * Set the in node
#     * @param node the node
#     */
   def setInNode(self, node):
        self.inNode = node

#   /**
#    * Get the out node
#    * @return the node
#    */
   def getOutNode(self):
      return self.outNode
    
#    /**
#     * Set the out node
#     * @param node the node
#     */
   def setOutNode(self, node):
        self.outNode = node
   
#   /**
#    * Get the input value
#    * @return the value
#    */
   def getInValue(self):
      return self.inNode.getActivation()
   
#   /**
#    * Get the output value
#    * @return the value
#    */
   def getOutValue(self):
      return self.outNode.getActivation()
   
#   /**
#    * Get the weighted out value
#    * @return the weighted out value
#    */
   def getWeightedOutValue(self):
      return self.outNode.getActivation() * self.weight
   
#   /**
#    * Get the weighted in value
#    * @return the value
#    */
   def getWeightedInValue(self):
      return float(self.inNode.getActivation()) * self.weight

#   /**
#    * Get the weight of the link
#    * @return the weight
#    */
   def getWeight(self):
      return self.weight

#   /**
#    * Set the weight of the link
#    * @param d the weight
#    */
   def setWeight(self, d):
      self.weight = d

#   /**
#    * Update the weight
#    * @param delta the change in weight
#    */
   def changeWeight(self, delta):
      self.weight = self.weight + delta
