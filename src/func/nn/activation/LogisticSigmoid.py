import math
#/**
#* A sigmoid activation function
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
class LogisticSigmoid():

#/**
#* @see nn.function.ActivationFunction#activation(double)
#*/
   def value(self, value):
        enx = math.exp(-value)
        if (math.isinf(enx)):
            return 0
        else:
            return 1.0 / (1.0 + enx)        


#	/**
#	 * @see nn.function.DifferentiableActivationFunction#derivative(double)
#	 */
   def derivative(self, value):
        logistic = value(value)
        return logistic * (1 - logistic)
