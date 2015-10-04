

#/**
#* A polynomial kernel
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class PolynomialKernel extends Kernel {
#/**
#* The weight of the dot product
#*/
    double dotProductWeight
    
#/**
#* The constant added on
#*/
    double additiveConstant

#/**
#* The exponent in the polynomial
#*/
    int exponent
    
#/**
#* Make a new polynomial kernel
#* @param dotProductWeight the weight to give to the dot product term
#* @param additiveConstant the additive constant
#* @param exponent the exponent
#*/
     PolynomialKernel(double dotProductWeight, double additiveConstant,
           int exponent):
        self.dotProductWeight = dotProductWeight
        self.additiveConstant = additiveConstant
        self.exponent = exponent
    }

#/**
#* Make a new polynomial kernel
#* @param exponent the exponent
#*/
     PolynomialKernel(int exponent):
        self(exponent, false)
    }
    
#/**
#* Make a new polynomial kernel
#* @param exponent the exponent
#* @param addOne whether to add one to the polynomial
#*/
     PolynomialKernel(int exponent, boolean addOne):
        self(1,0,exponent)
        if (addOne):
            additiveConstant = 1
        }
    }

#/**
#* @see svm.Kernel#value(svm.SupportVectorMachineData, svm.SupportVectorMachineData)
#*/
     double value(Instance a, Instance b):
        return Math.pow(dotProductWeight * a.getData().dotProduct(b.getData()) 
            + additiveConstant, exponent)
    }
    
#/**
#* @see java.lang.Object#toString()
#*/
     String toString():
        return "Polynomial Kernel (" + dotProductWeight + "*K(xi,xj) + " + additiveConstant
            + ")^" + exponent
    }


}
