from src.func.nn.feedfwd.FeedForwardNetwork import *
from src.func.nn.Layer import *
#/**
#* A back propagation network
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
class BackPropagationNetwork(FeedForwardNetwork):

#/**
#* Backpropagte through the network.
#*/
   def backpropagate(self):
      self.getOutputLayer().backpropagate()
      for i in reversed(range(self.getHiddenLayerCount() - 1)):
         self.getHiddenLayer(i).backpropagate()


#	/**
#* Clear out the error values at the end of a batch
#	 * or at the end of a single training for
#* stochastic / online training
#	 */
   def clearError(self):
     self.getOutputLayer().clearError()
     for i in reversed(range(self.getHiddenLayerCount() - 1)):
         self.getHiddenLayer(i).clearError()

#/**
#* Update weights with the given rule
#* @param rule the rule to use to update weights
#*/
   def updateWeights(self, rule):
     self.getOutputLayer().updateWeights(rule)
     for i in reversed(range(self.getHiddenLayerCount() - 1)):
         self.getHiddenLayer(i).updateWeights(rule)

 
#/**
#* Set the output errors
#* @param errors the output errors
#*/
   def setOutputErrors(self, errors):
     self.getOutputLayer().setOutputErrors(errors)

