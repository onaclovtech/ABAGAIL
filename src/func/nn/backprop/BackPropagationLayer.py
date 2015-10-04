

#/**
#* A layer in a backpropagation network
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class BackPropagationLayer extends FeedForwardLayer {
    
#/**
#* Back propagate all the error values for self
#* layer.
#*/
      backpropagate():
        for (int i = 0 i < getNodeCount() i++):
            BackPropagationNode node =
                 (BackPropagationNode) getNode(i)
            node.backpropagate()
            node.backpropagateLinks()
        }
    }
    
#/**
#* Clear out the error derivatives in the weights
#*/
      clearError():
        for (int i = 0 i < getNodeCount() i++):
            ((BackPropagationNode) getNode(i)).clearError()
        }
    }
    
#/**
#* Update weights with the given rule
#* @param rule the rule to use
#*/
      updateWeights(WeightUpdateRule rule):
        for (int i = 0 i < getNodeCount() i++):
            ((BackPropagationNode) getNode(i)).updateWeights(rule)
        }
    }
    
#/**
#* Set the output errors for self layer
#* @param errors the output errors
#*/
      setOutputErrors(double[] errors):
        for (int i = 0 i < getNodeCount() i++):
            ((BackPropagationNode) getNode(i)).setOutputError(errors[i])
        }
    }
    
}
