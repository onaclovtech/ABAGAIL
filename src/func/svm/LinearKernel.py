

#/**
#* A linear support vector machine kernel
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class LinearKernel extends Kernel {

#/**
#* @see svm.Kernel#value(shared.Instance, shared.Instance)
#*/
     double value(Instance a, Instance b):
        return a.getData().dotProduct(b.getData())
    }
    
#/**
#* @see java.lang.Object#toString()
#*/
     String toString():
        return "Linear Kernel"
    }

}
