



#/**
#* A back propagation node
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class BackPropagationNode extends FeedForwardNode {

#/**
#* The derivative of the error with respect to
#* the activation of self node.
#*/
    double inputError
    
#/**
#* The deriviative of the error with respect to
#* the activation of self node.
#*/
    double outputError
    
	/**
	 * Create a new back propogation node
	 * @param function the differentiable activation function
	 * @param learningRate the learning rate
	 * @param momentum the momentum
	 */
	 BackPropagationNode(DifferentiableActivationFunction function):
	    super(function)
    }

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
	  backpropagate():
        if  (getOutLinkCount() > 0):
            double weightedErrorSum = 0
            for (int i = 0 i < getOutLinkCount() i++):
                BackPropagationLink outLink = 
                    (BackPropagationLink) getOutLink(i)
                weightedErrorSum += outLink.getWeightedOutError()
            }
            setOutputError(weightedErrorSum)
            DifferentiableActivationFunction act =
                (DifferentiableActivationFunction) getActivationFunction()
            setInputError(act.derivative(getWeightedInputSum()) * getOutputError())
        } else {
            setInputError(getOutputError())
        }
    }

#/**
#* Backpropagate error into the incoming links 
#* from self node
#*/
      backpropagateLinks():
        for (int i = 0 i < getInLinkCount() i++):
            BackPropagationLink inLink = 
                (BackPropagationLink) getInLink(i) 
            inLink.backpropagate()
        }
    }

#/**
#* Update the incoming weights with the given rule
#* @param rule the rule to use
#*/
      updateWeights(WeightUpdateRule rule):
        for (int i = 0 i < getInLinkCount() i++):
            BackPropagationLink inLink = 
                (BackPropagationLink) getInLink(i) 
            rule.update(inLink)
        }
    }

#/**
#* Set the error for self node with respect to
#* the output of the node
#* @param error the new error value
#*/
      setOutputError(double error):
        outputError = error
    }
    
#/**
#* Get the error for self node with respect
#* to the output of the node
#* @return the error
#*/
     double getOutputError():
        return outputError
    }

#/**
#* Get the error for self node with respect to
#* the weighted input of the node
#* @return the error
#*/
     double getInputError():
        return inputError
    }
    
#/**
#* Set the error with respect
#* to the weighted input of the node
#* @param error the error
#*/
      setInputError(double error):
        inputError = error
    }
        
#/**
#* Clears all of the error derivatives for
#* the incoming links.
#*/
      clearError():
        for (int i = 0 i < getInLinkCount() i++):
            BackPropagationLink inLink = 
                (BackPropagationLink) getInLink(i) 
            inLink.clearError()
        }
    }

    
#/**
#* @see nn.Node#createLink()
#*/
     Link createLink():
        return new BackPropagationLink()
    }

}
