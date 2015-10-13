


#/**
#* A interface for distributions
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
class Distribution: 
#/**
#* A random number generator
#*/
     static final Random random = new Random()  
#/**
#* Get the probability of i
#* @param i the discrete value to get the probability of
#* @return the probability of i
#*/
     abstract double p(Instance i)
#/**
#* Calculate the log likelihood
#* @param i the instance
#* @return the log likelihood
#*/
     abstract double logp(Instance i)
    
#/**
#* Generate a random value
#* @param i the conditional values or null
#* @return the value
#*/
     abstract Instance sample(Instance i)
    
#/**
#* Generate a random value
#* @return the value
#*/
     abstract Instance sample()
    
#/**
#* Get the mode of the distribution
#* @param i the instance
#* @return the mode
#*/
     abstract Instance mode(Instance i)
    
#/**
#* Get the mode of the distribution
#* @return the mode
#*/
     abstract Instance mode()
    
#/**
#* Estimate the distribution from data
#* @param set the data set to estimate from
#*/
     abstract  estimate(DataSet set)

}