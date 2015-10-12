from src.func.nn.NeuralNetwork import *
from src.func.nn.Layer import *
#/**
# * A layered neural network
# * @author Andrew Guillory gtg008g@mail.gatech.edu
# * @version 1.0
# */
class LayeredNetwork(NeuralNetwork):
   
#   /**
#    * Make a layered network
#    */
   def __init__(self):
      self.hiddenLayers = []
      self.inputLayer = Layer()
      self.outputLayer = Layer()
      self.links = [];

#   /**   
#     * @see Network#getOutputValues()
#     */
   def getOutputValues(self):
      #print "layeredNetwork.getOutputValues().self.outputLayer.getActivations().toString()" + str(self.outputLayer.getActivations().toString())
      return self.outputLayer.getActivations()
   
#   /**
#    * @see Network#setInputValues(double[])
#    */
   def setInputValues(self, values):
      if not isinstance(values, Vector):
         raise TypeError('Need a Vector Type: ' + str(values))
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

#   /**
#    * Get the input layer
#    * @return the layer
#    */
   def getInputLayer(self):
      return self.inputLayer

#   /**
#    * Get the list of middle layers
#    * @return the list
#    */
   def getHiddenLayers(self):
      return self.hiddenLayers

#   /**
#    * Get the output layer
#    * @return the layer
#    */
   def getOutputLayer(self):
      return self.outputLayer

#   /**
#    * Set the input layer
#    * @param layer the layer
#    */
   def setInputLayer(self, layer):
      self.inputLayer = layer

#   /**
#    * Set the output layer
#    * @param layer the output layer
#    */
   def setOutputLayer(self, layer):
      self.outputLayer = layer

#   /**
#    * Get the middle layer count
#    * @return the middle layer count
#    */
   def getHiddenLayerCount(self):
      return len(self.hiddenLayers)
   
#   /**
#    * Get the middle layer
#    * @param i the index of the middle layer
#    * @return the layer
#    */
   def getHiddenLayer(self, i):
      #print "layeredNetwork.getHiddenLayer.self.hiddenLayers[i].__class__" + str(self.hiddenLayers[i].__dict__)
      return self.hiddenLayers[i] # Returns a layer, dunno
   
#   /**
#    * Add a middle layer
#    * @param layer the layer to add
#    */
   def addHiddenLayer(self, layer):
      self.hiddenLayers.append(layer)

#   /**
#    * Disconnect this network
#    */
   def disconnect(self):
      if (self.inputLayer != None and self.getHiddenLayerCount() > 0):
         firstMiddle = self.getHiddenLayer(0)
         self.inputLayer.disconnect(firstMiddle)
      else:
         if (self.inputLayer != None and self.outputLayer != None):
            self.inputLayer.disconnect(self.outputLayer)
      #for (i = 0; i + 1 < self.getHiddenLayerCount(); i++):
      for i in range(self.getHiddenLayerCount() - 1):
         first = self.getHiddenLayer(i)
         second = self.getHiddenLayer(i + 1)
         first.disconnect(second)
      if (self.outputLayer != None and self.getHiddenLayerCount() > 0):
         lastMiddle = getHiddenLayer(getHiddenLayerCount() - 1)
         lastMiddle.disconnect(outputLayer)
#   /**
#    * Connect this network
#    */
   def connect(self):
      if (self.inputLayer != None and self.getHiddenLayerCount() > 0):
         firstMiddle = self.getHiddenLayer(0)
         self.inputLayer.connect(firstMiddle)
      else:
         if (not self.inputLayer is None and not self.outputLayer is None):
            self.inputLayer.connect(self.outputLayer)
      #for (int i = 0; i  < self.getHiddenLayerCount() - 1; i++): Did I implement right?
      for i in range(self.getHiddenLayerCount() - 1):
         first = self.getHiddenLayer(i)
         second = self.getHiddenLayer(i + 1)
         first.connect(second)
      if (not self.outputLayer is None and self.getHiddenLayerCount() > 0):
         lastMiddle = self.getHiddenLayer(self.getHiddenLayerCount() - 1)
         lastMiddle.connect(self.outputLayer)
#    /**
#     * @see nn.NeuralNetwork#getLinks()
#     */
   def getLinks(self):
       if not isinstance(self.links, list):
           return self.links
       self.links.append(self.inputLayer.getLinks())
       for i in range(self.getHiddenLayerCount()):
           self.links.append(self.getHiddenLayer(i).getLinks())
       self.links.append(self.outputLayer.getLinks())
       return self.links
