from src.util.linalg.DenseVector import *
#/**
# * A layer is a collection of nodes
# * @author Andrew Guillory gtg008g@mail.gatech.edu
# * @version 1.0
# */
class Layer:

#   /**
#    * Make a empty layer
#    */
   def __init__(self):
      self.nodes = []

#   /**
#    * Get the node count
#    * @return the number of nodes
#    */
   def getNodeCount(self):
      return len(self.nodes)
   
#   /**
#    * Get the node i
#    * @param i the node to get
#    * @return the node
#    */
   def getNode(self, i):
      return self.nodes[i]
   
#   /**
#    * Add a node
#    * @param node the node to add
#    */
   def addNode(self, node):
      self.nodes.append(node)
   
#   /**
#    * Set the values
#    * @param values the values
#    */
   def setActivations(self, values):
      for i in range(values.size()):
         self.getNode(i).setActivation(values.get(i))
   
#   /**
#    * Get the list of values in this layer
#    * @return the list of values
#    */
   def getActivations(self):
      values = [self.getNodeCount()];
      for i in range(len(values)):
         values[i] = self.getNode(i).getActivation()
      return DenseVector(values)

    
#    /**
#     * Get the index of the node with the largest activation
#     * @return the index
#     */
   def getGreatestActivationIndex(self):
        largest = 0;
        largestValue = getNode(largest).getActivation()
        for i in range(self.getNodeCount()):
            if (getNode(i).getActivation() > largestValue):
                largest = i
                largestValue = getNode(largest).getActivation()
        return largest

#   /**
#    * Connect to another layer
#    * @param layer the layer to connect to
#    */
   def connect(self, layer):
      for i in range(self.getNodeCount()):
         node = self.getNode(i)
         for j in range(layer.getNodeCount()):
            node.connect(layer.getNode(j))

#   /**
#    * Disconnect with another layer
#    * @param layer the layer to disconnect with
#    */
   def disconnect(self, layer):
      for i in range(getNodeCount()):
         node = getNode(i)
         for j in range(layer.getNodeCount()):
            node.disconnect(layer.getNode(i))
    
#    /**
#     * Get all of the links going into this layer
#     * @return all of the links
#     */
   def getLinks(self):
        links = []
        for i in range(len(self.nodes)):
            n = self.nodes[i]
            links.append(n.getInLinks())
        return links
