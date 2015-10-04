

#/**
#* An abstract condtional distribution
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 abstract class AbstractConditionalDistribution extends AbstractDistribution (ConditionalDistribution):

#/**
#* Generate a output given the input
#* @param i the input
#* @return the output
#*/
     Instance sample(Instance i):
        return distributionFor(i).sample()
    }
    
#/**
#* Generate a output that is most likely given the input
#* @param i the input
#* @return the output
#*/
     Instance mode(Instance i):
        return distributionFor(i).sample()
    }
    
#/**
#* Probability of an instance
#* @parma i the instance
#* @return the probability
#*/
     double p(Instance i):
        return distributionFor(i).p(i.getLabel())
    }
}
