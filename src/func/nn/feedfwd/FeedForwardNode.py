



#/**
#* A node in a feed forward network
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class FeedForwardNode extends Neuron {

	/**
	 * The transfer function
	 */
	ActivationFunction activationFunction
    
#/**
#* The weighted input sum
#*/
    double weightedInputSum

	/**
	 * Make a new feed forward node
	 * @param transfer the transfer function
	 */
	 FeedForwardNode(ActivationFunction transfer):
		activationFunction = transfer
	}
	
	/**
	 * Get the transfer function
	 * @return the transfer function
	 */
	 ActivationFunction getActivationFunction():
		return activationFunction
	}

#/**
#* Get the weighted input sum for self node
#* @return the weighted input sum
#*/
     double getWeightedInputSum():
        return weightedInputSum
    }

#/**
#* Feed forward the activation values into self node.
#* Calculates the sum of the input values and stores
#* self value into weightedInputSum.
#* Runs self sum through the activation function
#* and stores self into the activation for the node.
#*/
	  feedforward():
		if (getInLinkCount() > 0):
			double sum = 0
			for (int i = 0 i < getInLinkCount() i++):
				sum += getInLink(i).getWeightedInValue()
			}
            weightedInputSum = sum
			setActivation(activationFunction.value(sum))
		}
	}

}
