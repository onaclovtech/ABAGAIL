from src.func.nn.Neuron import *
import inspect

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
      Neuron.__init__(self)
      self.activationFunction = transfer
      self.weightedInputSum = 0.0
   
   # /**
    # * Get the transfer function
    # * @return the transfer function
    # */
   def getActivationFunction(self):
      return self.activationFunction
   
   

#/**
#* Get the weighted input sum for self node
#* @return the weighted input sum
#*/
   def getWeightedInputSum(self):
        return self.weightedInputSum
    

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
            sum = sum + self.getInLink(i).getWeightedInValue()
         weightedInputSum = sum
         #print inspect.getmro(self.__class__)
         #print self.__dict__
         #print sum
         self.setActivation(self.activationFunction.value(sum))

#<class src.func.nn.backprop.BackPropagationBiasNode.BackPropagationBiasNode at 0x014A1688>, 
#<class src.func.nn.backprop.BackPropagationNode.BackPropagationNode at 0x014A1340>, 
#<class src.func.nn.feedfwd.FeedForwardNode.FeedForwardNode at 0x014A1298>, 
#<class src.func.nn.Neuron.Neuron at 0x014A11B8>)

# {'activation': 1, 
# 'outLinks': [<src.func.nn.backprop.BackPropagationLink.BackPropagationLink instance at 0x01A995A8>, 
             # <src.func.nn.backprop.BackPropagationLink.BackPropagationLink instance at 0x01A99530>, 
             # <src.func.nn.backprop.BackPropagationLink.BackPropagationLink instance at 0x01A995F8>, 
             # <src.func.nn.backprop.BackPropagationLink.BackPropagationLink instance at 0x01A99580>, 
             # <src.func.nn.backprop.BackPropagationLink.BackPropagationLink instance at 0x01A99648>, 
             # <src.func.nn.backprop.BackPropagationLink.BackPropagationLink instance at 0x01A995D0>], 
# 'activationFunction': None, 
# 'weightedInputSum': 0.0, 
# 'inLinks': [<src.func.nn.backprop.BackPropagationLink.BackPropagationLink instance at 0x014D1030>, 
            # <src.func.nn.backprop.BackPropagationLink.BackPropagationLink instance at 0x014D13A0>, 
            # <src.func.nn.backprop.BackPropagationLink.BackPropagationLink instance at 0x014D1C88>,
            # <src.func.nn.backprop.BackPropagationLink.BackPropagationLink instance at 0x0151B918>, 
            # <src.func.nn.backprop.BackPropagationLink.BackPropagationLink instance at 0x0151BA58>, 
            # <src.func.nn.backprop.BackPropagationLink.BackPropagationLink instance at 0x0151BB98>, 
            # <src.func.nn.backprop.BackPropagationLink.BackPropagationLink instance at 0x0151BCD8>, 
            # <src.func.nn.backprop.BackPropagationLink.BackPropagationLink instance at 0x0151BE18>]}