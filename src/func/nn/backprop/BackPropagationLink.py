from src.func.nn.Link import *
#/**
#* 
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
class BackPropagationLink(Link):

#/**
#* The derivative of the error function
#* in respect to self node, or in the case
#* of batch training possibly the sum
#* of derivative of the error functions for
#* many patterns.
#*/
   # double error
    
#/**
#* The last derivative of the error function
#* in respect to self node, sometimes
#* used in training algorithms that use
#* momentum type terms.
#*/
   # double lastError
    
#/**
#* The last change made to self link (last delta),
#* sometimes used in algorithms with momentum
#* type terms.
#*/
   # double lastChange
    
#/**
#* A learning rate term which is used in
#* some algorithms that have weight specific
#* learning rates.
#*/
   # double learningRate
    
#/**
#* @see nn.Link#changeWeight(double)
#*/
   def changeWeight(self, delta):
         super.changeWeight(delta)
         lastChange = delta
    
#/**
#* Backpropagate error values into self link
#*/
   def backpropagate(self):
        addError(getInValue() * getOutError())
    
    
#/**
#* Add error to self link
#* @param error the error to add
#*/
   def addError(self, error):
        self.error = self.error + error
    
    
#/**
#* Clear out the error and 
#* set the current error to be the last error
#*/
   def clearError(self):
        lastError = error
        error = 0
    
    
#/**
#* Get the error derivative with respect to self weight
#* @return the error derivative value
#*/
   def getError(self):
        return error
    
    
#/**
#* Set the error
#* @param error the error to set
#*/
   def setError(self, error):
    	self.error = error
    

#/**
#* Get the last change in the weight
#* @return the last change in weight
#*/
   def getLastChange(self):
        return lastChange
    

#/**
#* Get the last error value
#* @return the last error value
#*/
   def getLastError(self):
        return lastError
    
    
#/**
#* Set the learning rate
#* @param learningRate the learning rate
#*/
   def setLearningRate(self, learningRate):
        self.learningRate = learningRate
    

#/**
#* Get the learning rate
#* @return the learning rate
#*/
   def getLearningRate(self):
        return learningRate
    
    
#/**
#* Get the output error
#* @return the output error
#*/
   def getOutError(self):
        return self.getOutNode().getInputError()
    
    
#/**
#* Get the weighted output error
#* @return the output error times the weigh tof the link
#*/
   def getWeightedOutError(self):
        return self.getOutNode().getInputError()
#* getWeight()
    
    
#/**
#* Get the input error
#* @return the input error
#*/
   def getInError(self):
        return self.getInNode().getInputError()
    

#/**
#* Get the weighted input error
#* @return the weighted error
#*/
   def getWeightedInError(self):
        return self.getInNode().getInputError()
#* getWeight()

