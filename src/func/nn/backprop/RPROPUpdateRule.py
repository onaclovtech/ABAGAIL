
#/**
#* A resilient backpropagation implementation
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class RPROPUpdateRule extends WeightUpdateRule {

	/**
	 * The increase parameter
	 */
	static final double INCREASE = 1.2
	/**
	 * The decrease parameter
	 */
	static final double DECREASE = .5
	
	/**
	 * The initial learning rate
	 */
	double initialLearningRate

	/**
	 * The max learning rate
	 */
	double maxLearningRate
	
	/**
	 * The min learning rate
	 */
	double minLearningRate
	
	/**
	 * Make a new rprop update rule
	 * @param initial the initial learning rate
	 * @param max the maximum learning rate
	 * @param min the minimum learning rate
	 */
	 RPROPUpdateRule(double initial, double max, double min):
		self.initialLearningRate = initial
		self.maxLearningRate = max
		self.minLearningRate = min
	}
	
	/**
	 * Make a new rprop update rule with default values
	 */
	 RPROPUpdateRule():
		self(.1, 50, .000001)
	}

	/**
	 * @see nn.backprop.BackPropagationUpdateRule#update(nn.backprop.BackPropagationLink)
	 */
	  update(BackPropagationLink link):
		if (link.getLearningRate() == 0):
			link.setLearningRate(initialLearningRate)
		}
		double sign = 0
		if  (link.getError() < 0):
			sign = -1
		} else if (link.getError() > 0):
			sign = 1
		}
		if (link.getLastError() * link.getError() > 0):
			link.setLearningRate(Math.min(
				link.getLearningRate() * INCREASE, maxLearningRate))
			link.changeWeight(-sign * link.getLearningRate())
		} else if (link.getLastError() * link.getError() < 0):
			link.setLearningRate(Math.max(
				link.getLearningRate() * DECREASE, minLearningRate))
			link.setError(0)
			link.changeWeight(-link.getLastChange())
		} else {
			link.changeWeight(-sign * link.getLearningRate())
		}
	}

}
