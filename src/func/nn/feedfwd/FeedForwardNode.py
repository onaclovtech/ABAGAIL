from src.func.nn.Neuron import *


#/**
#* A node in a feed forward network
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
class FeedForwardNode(Neuron):

   # /**
    # * The transfer function
    # */
   # ActivationFunction activationFunction
    
#/**
#* The weighted input sum
#*/
    # double weightedInputSum

   # /**
    # * Make a new feed forward node
    # * @param transfer the transfer function
    # */
   def __init__(self, transfer = None):
      activationFunction = transfer
   
   
   # /**
    # * Get the transfer function
    # * @return the transfer function
    # */
   def getActivationFunction(self):
      return activationFunction
   

#/**
#* Get the weighted input sum for self node
#* @return the weighted input sum
#*/
   def getWeightedInputSum(self):
        return weightedInputSum
    

#/**
#* Feed forward the activation values into self node.
#* Calculates the sum of the input values and stores
#* self value into weightedInputSum.
#* Runs self sum through the activation function
#* and stores self into the activation for the node.
#*/
   def feedforward(self):
      if (self.getInLinkCount() > 0):
         sum = 0
         for i in range(self.getInLinkCount()):
            sum += self.getInLink(i).getWeightedInValue()
         weightedInputSum = sum
         setActivation(activationFunction.value(sum))

