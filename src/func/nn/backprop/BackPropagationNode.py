from src.func.nn.feedfwd.FeedForwardNode import *
from src.func.nn.backprop.BackPropagationLink import *

#/**
#* A back propagation node
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
class BackPropagationNode(FeedForwardNode):

#/**
#* The derivative of the error with respect to
#* the activation of self node.
#*/
    #double inputError
    
#/**
#* The deriviative of the error with respect to
#* the activation of self node.
#*/
    #double outputError
    
#    /**
#     * Create a back propogation node
#     * @param function the differentiable activation function
#     * @param learningRate the learning rate
#     * @param momentum the momentum
#     */
   def __init__(self, transfer = None):
      self.transfer = transfer
      self.outLinks = []
      self.inLinks = []
#/**
#* Back propagate error values.
#* For nodes that have output links, first
#* calculates the derivative of the error function
#* with respect to self node by finding the weighted
#* sum of the errors of nodes self node outputs to, 
#* and multiplying that by the derivative of the activation
#* function applied to the weighted input sum.
#* For nodes with output links, simply moves the error
#* to the output (assuming that the appropriate error
#* function / activation function combination was
#* used).
#*/
   def backpropagate(self):
        if  (getOutLinkCount() > 0):
            weightedErrorSum = 0
            for i in range(getOutLinkCount()):
                outLink = getOutLink(i)
                weightedErrorSum += outLink.getWeightedOutError()
            
            setOutputError(weightedErrorSum)
            act = getActivationFunction()
            setInputError(act.derivative(getWeightedInputSum()) * getOutputError())
        else:
            setInputError(getOutputError())
        

#/**
#* Backpropagate error into the incoming links 
#* from self node
#*/
   def backpropagateLinks(self):
        for i in range(getInLinkCount()):
            inLink = getInLink(i) 
            inLink.backpropagate()
       

#/**
#* Update the incoming weights with the given rule
#* @param rule the rule to use
#*/
   def updateWeights(self, rule):
        for i in range(getInLinkCount()):
            inLink = getInLink(i) 
            rule.update(inLink)
     

#/**
#* Set the error for self node with respect to
#* the output of the node
#* @param error the error value
#*/
   def setOutputError(self, error):
        outputError = error
    
    
#/**
#* Get the error for self node with respect
#* to the output of the node
#* @return the error
#*/
   def getOutputError(self):
        return outputError
    

#/**
#* Get the error for self node with respect to
#* the weighted input of the node
#* @return the error
#*/
   def getInputError(self):
        return inputError
    
    
#/**
#* Set the error with respect
#* to the weighted input of the node
#* @param error the error
#*/
   def setInputError(self, error):
        inputError = error
    
        
#/**
#* Clears all of the error derivatives for
#* the incoming links.
#*/
   def clearError(self):
        for i in range(getInLinkCount()):
            inLink = getInLink(i) 
            inLink.clearError()
       

    
#/**
#* @see nn.Node#createLink()
#*/
   def createLink(self):
        return BackPropagationLink()
   
