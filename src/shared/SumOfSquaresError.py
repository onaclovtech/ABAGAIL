from src.shared.AbstractErrorMeasure import *


#/**
#* Standard error measure, suitable for use with
#* linear output networks for regression, sigmoid
#* output networks for single class probability,
#* and soft max networks for multi class probabilities.
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
class SumOfSquaresError(AbstractErrorMeasure):

#/**
#* @see nn.error.ErrorMeasure#error(double[], nn.Pattern[], int)
#*/
     def value(self, output, example):
        sum = 0
        label = example.getLabel()
        for i in range(output.size()):
            sum += (output.getContinuous(i) - label.getContinuous(i)) * (output.getContinuous(i) - label.getContinuous(i)) * example.getWeight()
        
        return .5 * sum
    

#/**
#* @see nn.error.DifferentiableErrorMeasure#derivatives(double[], nn.Pattern[], int)
#*/
     def gradient(self, output, example):      
        errorArray = double[output.size()]
        label = example.getLabel()
        for i in range(len(output)):
            errorArray[i] = (output.getContinuous(i) - label.getContinuous(i))
#* example.getWeight()
        return errorArray
