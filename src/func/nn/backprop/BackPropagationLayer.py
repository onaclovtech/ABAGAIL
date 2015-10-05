from src.func.nn.feedfwd.FeedForwardLayer import *

#/**
#* A layer in a backpropagation network
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
class BackPropagationLayer(FeedForwardLayer):
    
#/**
#* Back propagate all the error values for self
#* layer.
#*/
      def __init__(self):
         self.nodes = []
         
      def backpropagate(self):
        for i in range(self.getNodeCount()):
            node = self.getNode(i)
            node.backpropagate()
            node.backpropagateLinks()
    
#/**
#* Clear out the error derivatives in the weights
#*/
      def clearError(self):
        for i in range(self.getNodeCount()):
            self.getNode(i).clearError()
    
#/**
#* Update weights with the given rule
#* @param rule the rule to use
#*/
      def updateWeights(self, rule):
        for i in range(self.getNodeCount()):
            self.getNode(i).updateWeights(rule)
    
#/**
#* Set the output errors for self layer
#* @param errors the output errors
#*/
      def setOutputErrors(self, errors):
        for i in range(self.getNodeCount()):
            self.getNode(i).setOutputError(errors[i])