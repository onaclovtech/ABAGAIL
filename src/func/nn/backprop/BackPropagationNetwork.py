



#/**
#* A back propagation network
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class BackPropagationNetwork extends FeedForwardNetwork {

#/**
#* Backpropagte through the network.
#*/
	  backpropagate():
		((BackPropagationLayer) getOutputLayer()).backpropagate()
		for (int i = getHiddenLayerCount() - 1 i >= 0 i--):
			((BackPropagationLayer) getHiddenLayer(i)).backpropagate()
		}
	}

	/**
#* Clear out the error values at the end of a batch
	 * or at the end of a single training for
#* stochastic / online training
	 */
      clearError():
        ((BackPropagationLayer) getOutputLayer()).clearError()
        for (int i = getHiddenLayerCount() - 1 i >= 0 i--):
            ((BackPropagationLayer) getHiddenLayer(i)).clearError()
        }
    }
    
#/**
#* Update weights with the given rule
#* @param rule the rule to use to update weights
#*/
      updateWeights(WeightUpdateRule rule):
        ((BackPropagationLayer) getOutputLayer()).updateWeights(rule)
        for (int i = getHiddenLayerCount() - 1 i >= 0 i--):
            ((BackPropagationLayer) getHiddenLayer(i)).updateWeights(rule)
        }
    }
    
#/**
#* Set the output errors
#* @param errors the output errors
#*/
      setOutputErrors(double[] errors):
        ((BackPropagationLayer) getOutputLayer()).setOutputErrors(errors)
    }




}
