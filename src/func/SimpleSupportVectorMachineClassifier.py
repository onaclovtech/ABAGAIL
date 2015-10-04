

#/**
#* 
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class SimpleSupportVectorMachineClassifier extends AbstractConditionalDistribution (FunctionApproximater):
    
#/**
#* The svm itself
#*/
    SupportVectorMachine svm
    
#/**
#* The kernel
#*/
    Kernel kernel
    
#/**
#* The c value
#*/
    double c
    
#/**
#* Make a new svm classifier
#*/
     SimpleSupportVectorMachineClassifier():
        self(1, new LinearKernel())
    }
    
#/**
#* Make a new svm classifier
#* @param c the c value
#* @param kernel the kernel
#*/
     SimpleSupportVectorMachineClassifier(double c, 
            Kernel kernel):
        self.c = c
        self.kernel = kernel            
    }

#/**
#* @see func.FunctionApproximater#estimate(shared.DataSet)
#*/
      estimate(DataSet set):
        DiscreteToBinaryFilter dtbf = new DiscreteToBinaryFilter()
        dtbf.filter(set)
        SequentialMinimalOptimization smo = 
            new SequentialMinimalOptimization(set, kernel, c)
	smo.train()
        svm = smo.getSupportVectorMachine()
    }

#/**
#* @see func.FunctionApproximater#value(shared.Instance)
#*/
     Instance value(Instance i):
        return svm.value(i)
    }
    
#/**
#* @see func.Classifier#classDistribution(shared.Instance)
#*/
     Distribution distributionFor(Instance data):
        Instance v = value(data)
        double[] p = new double[2]
        p[v.getDiscrete()] = 1
        return new DiscreteDistribution(p)
    }

#/**
#* Get the c value
#* @return the c value
#*/
     double getC():
        return c
    }

#/**
#* Get the kernel
#* @return the kernel
#*/
     Kernel getKernel():
        return kernel
    }

#/**
#* Set the c value
#* @param d the new c value
#*/
      setC(double d):
        c = d
    }

#/**
#* Set the kernel function
#* @param kernel the new kernel function
#*/
      setKernel(Kernel kernel):
        self.kernel = kernel
    }

}
