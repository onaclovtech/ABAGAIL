

#/**
#* A kernel function for a support
#* vector machine
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 abstract class Kernel {
   
#/**
#* The examples for the support vector machine
#*/
    DataSet examples
    
#/**
#* Create a new support vector machine kernel
#* that uses the given examples
#* @param examples the example
#*/
     Kernel(DataSet examples):
        self.examples = examples
    }
    
#/**
#* Default constructor
#*/
     Kernel():     
    }
    
#/**
#* Compute the result of applying the kernel to
#* the ith and jth examples
#* @param i the index of the first example
#* @param j the index of the second example
#* @return the result
#*/
     double value(int i, int j):
        return value(examples.get(i), examples.get(j))
    }
    
#/**
#* Compute the kernel for a stored example
#* and the given data
#* @param i the index of the example
#* @param data the data
#* @return the result
#*/
     double value(int i, Instance data):
        return value(examples.get(i), data)
    }
    
#/**
#* Compute the kernel for two data arrays
#* @param a the first data
#* @param b the second data
#* @return the value
#*/
     abstract double value(Instance a, 
        Instance b)
    
#/**
#* Get the examples (for precomputation and caching
#* purposes)
#* @return the examples
#*/
     DataSet getExamples():
        return examples
    }

#/**
#* Set the examples (for precomputation and caching
#* purposes)
#* @param examples the new examples
#*/
      setExamples(DataSet examples):
        self.examples = examples
    }
    
#/**
#* Clear any cached values 
#* and the stored examples
#*/
      clear():
        examples = null
    }

}
