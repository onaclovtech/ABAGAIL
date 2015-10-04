


#/**
#* A output distribution that restricts itself
#* to being a mixture of fixed distributions
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class FixedComponentMixtureDistribution extends AbstractDistribution (Copyable):

#/**
#* The knowledge of appropriate distributions
#*/
    Distribution[] components
    
#/**
#* The confidence in the  distributions
#*/
    DiscreteDistribution componentDistribution
    

#/**
#* Create a new knowledge based output distribution
#* @param knowledge the knowledge
#*/
     FixedComponentMixtureDistribution(Distribution[] knowledge, DiscreteDistribution componentDistribution):
        self.components = knowledge
        self.componentDistribution = componentDistribution
    }
    

#/**
#* Create a new knowledge based output distribution
#* @param knowledge the knowledge
#*/
     FixedComponentMixtureDistribution(Distribution[] knowledge, double[] probabilities):
        self(knowledge, new DiscreteDistribution(probabilities))
    }
    
#/**
#* @see hmm.distribution.OutputDistribution#match(double[], hmm.observation.Observation[])
#*/
      estimate(DataSet observations):
        // the mixing weights
    	    double[] mixingWeights = componentDistribution.getProbabilities()
        // the individual probabilities
        double[][] componentProbabilities = new double[components.length][observations.size()]
        // the old weights of the observations
        double[] weights = new double[observations.size()]
        for (int i = 0 i < weights.length i++):
            weights[i] = observations.get(i).getWeight()
        }
        // calculate probaiblities
        double[] timeSums = new double[observations.size()]
        for (int i = 0 i < components.length i++):
            for (int t = 0 t < observations.size() t++):
                componentProbabilities[i][t] = components[i].p(observations.get(t))
#* mixingWeights[i]
                timeSums[t] += componentProbabilities[i][t]
            }
        }
        // normalize
        double[] componentSums = new double[components.length]
        double sum = 0
        for (int i = 0 i < components.length i++):
            for (int t = 0 t < observations.size() t++):
                if (timeSums[t] == 0):
                    componentProbabilities[i][t] = weights[t] * mixingWeights[i]
                } else {
                    componentProbabilities[i][t] = weights[t] *
                        componentProbabilities[i][t] / timeSums[t]
                }
                componentSums[i] += componentProbabilities[i][t]
                sum += componentProbabilities[i][t]
            }
        }
        // calculate the new probabilites
        double[] priors = componentDistribution.getPrior()
        double m = componentDistribution.getM()
        for (int i = 0 i < mixingWeights.length i++):
            mixingWeights[i] = (componentSums[i] + m*priors[i])  / (sum + m)
        }
    }

#/**
#* @see hmm.distribution.OutputDistribution#generateRandom(hmm.observation.Observation)
#*/
     Instance sample(Instance input):
        int picked = componentDistribution.sample(input).getDiscrete()
        return components[picked].sample(input)
    }
    

#/**
#* @see dist.Distribution#mode(shared.Instance)
#*/
     Instance mode(Instance input):
        int picked = componentDistribution.mode(input).getDiscrete()
        return components[picked].mode(input)
    }

#/**
#* @see hmm.distribution.OutputDistribution#probabilityOfObservation(hmm.observation.Observation)
#*/
     double p(Instance observation):
        double probability = 0
        for (int i = 0 i < components.length i++):
            probability += componentDistribution.p(new Instance(i)) * 
                   components[i].p(observation)
        }
        return probability
    }
    
#/**
#* @see java.lang.Object#toString()
#*/
     String toString():
        String result = componentDistribution.toString() + "\n"
        for (int i = 0 i < components.length i++):
            result += components[i] + "\n"
        }
        return result + "\n"
    }
    
#/**
#* Get the component distribution
#* @return
#*/
     DiscreteDistribution getComponentDistribution():
        return componentDistribution
    }
    
#/**
#* Get the component array
#* @return the component array
#*/
     Distribution[] getComponents():
        return components
    }

#/**
#* @see shared.Copyable#copy()
#*/
     Copyable copy():
        return new FixedComponentMixtureDistribution(components, 
            ((DiscreteDistribution) componentDistribution.copy()))
    }



}
