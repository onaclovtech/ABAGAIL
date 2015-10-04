

#/**
#* 
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 interface FunctionApproximater {
    
#/**
#* Estimate from the given data set
#* @param set the data set
#*/
      estimate(DataSet set)
    
#/**
#* Evaluate the function
#* @param i the input
#* @return the value
#*/
     Instance value(Instance i)

}
