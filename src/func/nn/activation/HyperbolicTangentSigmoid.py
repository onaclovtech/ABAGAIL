
#/**
#* The tanh sigmoid function
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class HyperbolicTangentSigmoid 
		extends DifferentiableActivationFunction{

#/**
#* @see nn.function.DifferentiableActivationFunction#derivative(double)
#*/
	 double derivative(double value):
		double tanhvalue = value(value)
		return 1 - tanhvalue * tanhvalue
	}

	/**
	 * @see nn.function.ActivationFunction#activation(double)
	 */
     double value(double value):
        double e2x = Math.exp(2 * value)
        if (e2x == Double.POSITIVE_INFINITY):
            return 1
        } else {
            return (e2x - 1) / (e2x + 1)
        }
	}
	

}
