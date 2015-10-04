

#/**
#* A activation function that is differentiable
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 abstract class DifferentiableActivationFunction extends ActivationFunction {	
	
	/**
	 * Perform the derivative of self function on the given value
	 * @param value the value to perform the derivative on
	 * @return the result
	 */
	 abstract double derivative(double value)
    
}
