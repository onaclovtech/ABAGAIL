

#/**
#* A polynomial kernel
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class SigmoidKernel extends Kernel {
#/**
#* The weight of the dot product
#*/
    double dotProductWeight
    
#/**
#* The constant added on
#*/
    double additiveConstant
    
#/**
#* Make a new sigmoid kernel
#* @param dotProductWeight the weight to give to the dot product term
#* @param additiveConstant the additive constant
#*/
     SigmoidKernel(double dotProductWeight, double additiveConstant):
        self.dotProductWeight = dotProductWeight
        self.additiveConstant = additiveConstant
    }
    
#/**
#* Make a new sigmoid kernel
#* @param addOne whether to add one to the sigmoid
#*/
     SigmoidKernel(boolean addOne):
        self(1,0)
        if (addOne):
            additiveConstant = 1
        }
    }
    
#/**
#* Make a new sigmoid kernel
#*/
     SigmoidKernel():
        self(false)
    }


#/**
#* @see svm.Kernel#value(svm.SupportVectorMachineData, svm.SupportVectorMachineData)
#*/
     double value(Instance a, Instance b):
        return tanh(dotProductWeight * a.getData().dotProduct(b.getData()) + additiveConstant)
    }
    
#/**
#* Compute the tanh of a value
#* @param value the value
#* @return the tanh
#*/
     double tanh(double value):
        double e2x = Math.exp(2 * value)
        if (e2x == Double.POSITIVE_INFINITY):
            return 1
        } else {
            return (e2x - 1) / (e2x + 1)
        }
    }
    
#/**
#* @see java.lang.Object#toString()
#*/
     String toString():
        return "Polynomial Kernel tanh(" + dotProductWeight + "*K(xi,xj) + " + additiveConstant
            + ")"
    }

}