#/**
#* An abstract error measure
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
class AbstractErrorMeasure:
#/**
#* Calculate the error between two data sets
#* @param a the first
#* @param b the second
#* @return the error
#*/
     def value(self, a, b):
        error = 0
        for i in range(len(a)):
            error += value(a.get(i), b.get(i))
        
        return error
    

