

#/**
#* A radial basis function kernel
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class RBFKernel extends Kernel {

#/**
#* The sigma parameter
#*/
    double sigma
    
#/**
#* The gamma value
#*/
    double gamma
    
#/**
#* Make a new radial basis function kernel
#* @param sigma the sigma value
#*/
     RBFKernel(double sigma):
        self.sigma = sigma
        gamma = -1/(2 * sigma * sigma)
    }


#/**
#* @see svm.Kernel#value(svm.SupportVectorMachineData, svm.SupportVectorMachineData)
#*/
     double value(Instance a, Instance b):
        Vector va = a.getData()
        Vector vb = b.getData()
        double difference = va.dotProduct(va)
            + vb.dotProduct(vb)
            - 2*va.dotProduct(vb)
        return Math.exp(gamma * difference)
    }

#/**
#* @see java.lang.Object#toString()
#*/
     String toString():
        return "RBF Kernel sigma = " + sigma
    }


}
