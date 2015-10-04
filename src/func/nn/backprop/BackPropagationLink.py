



#/**
#* 
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class BackPropagationLink extends Link {

#/**
#* The derivative of the error function
#* in respect to self node, or in the case
#* of batch training possibly the sum
#* of derivative of the error functions for
#* many patterns.
#*/
    double error
    
#/**
#* The last derivative of the error function
#* in respect to self node, sometimes
#* used in training algorithms that use
#* momentum type terms.
#*/
    double lastError
    
#/**
#* The last change made to self link (last delta),
#* sometimes used in algorithms with momentum
#* type terms.
#*/
    double lastChange
    
#/**
#* A learning rate term which is used in
#* some algorithms that have weight specific
#* learning rates.
#*/
    double learningRate
    
#/**
#* @see nn.Link#changeWeight(double)
#*/
      changeWeight(double delta):
         super.changeWeight(delta)
         lastChange = delta
    }
    
#/**
#* Backpropagate error values into self link
#*/
      backpropagate():
        addError(getInValue() * getOutError())
    }
    
#/**
#* Add error to self link
#* @param error the error to add
#*/
      addError(double error):
        self.error += error
    }
    
#/**
#* Clear out the error and 
#* set the current error to be the last error
#*/
      clearError():
        lastError = error
        error = 0
    }
    
#/**
#* Get the error derivative with respect to self weight
#* @return the error derivative value
#*/
     double getError():
        return error
    }
    
#/**
#* Set the error
#* @param error the error to set
#*/
      setError(double error):
    	self.error = error
    }

#/**
#* Get the last change in the weight
#* @return the last change in weight
#*/
     double getLastChange():
        return lastChange
    }

#/**
#* Get the last error value
#* @return the last error value
#*/
     double getLastError():
        return lastError
    }
    
#/**
#* Set the learning rate
#* @param learningRate the learning rate
#*/
      setLearningRate(double learningRate):
        self.learningRate = learningRate
    }

#/**
#* Get the learning rate
#* @return the learning rate
#*/
     double getLearningRate():
        return learningRate
    }
    
#/**
#* Get the output error
#* @return the output error
#*/
     double getOutError():
        return ((BackPropagationNode) getOutNode()).getInputError()
    }
    
#/**
#* Get the weighted output error
#* @return the output error times the weigh tof the link
#*/
     double getWeightedOutError():
        return ((BackPropagationNode) getOutNode()).getInputError()
#* getWeight()
    }
    
#/**
#* Get the input error
#* @return the input error
#*/
     double getInError():
        return ((BackPropagationNode) getInNode()).getInputError()
    }

#/**
#* Get the weighted input error
#* @return the weighted error
#*/
     double getWeightedInError():
        return ((BackPropagationNode) getInNode()).getInputError()
#* getWeight()
    }
}
