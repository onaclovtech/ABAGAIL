import math
#/**
#* The tanh sigmoid function
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
class HyperbolicTangentSigmoid:

#/**
#* @see nn.function.DifferentiableActivationFunction#derivative(double)
#*/
   def derivative(self, value):
      tanhvalue = value(value)
      return 1 - tanhvalue * tanhvalue
   

#   /**
#    * @see nn.function.ActivationFunction#activation(double)
#    */
   def value(self, value):
        e2x = math.exp(2 * value)
        if (math.isinf(e2x)):
            return 1
        else:
            return (e2x - 1) / (e2x + 1)
        
   
   


