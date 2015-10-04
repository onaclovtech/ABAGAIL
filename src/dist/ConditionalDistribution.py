

#/**
#* A conditional probability distribution
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 interface ConditionalDistribution extends Distribution {
    
#/**
#* Get the distribution for an instance
#* @param i the instance
#* @return the  distribution
#*/
     Distribution distributionFor(Instance i)

}
