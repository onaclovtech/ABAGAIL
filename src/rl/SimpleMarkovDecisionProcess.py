

#/**
#* A markov decision process with rewards unconditional on actions
#* implemented using an input output hidden markov model
#* @author Andrew Guillory gtg008g@mail.gatech.edu
#* @version 1.0
#*/
 class SimpleMarkovDecisionProcess extends ModularHiddenMarkovModel (MarkovDecisionProcess):
#/**
#* Set the reward values
#* @param rewardValues the reward values
#*/
      setRewards(double[] rewardValues):
        Distribution[] outputs = new Distribution[rewardValues.length]
        for (int i = 0 i < rewardValues.length i++):
            outputs[i] = new UnivariateGaussian(rewardValues[i], 1)
        }
        setOutputDistributions(outputs)
    }
    
#/**
#* Get the rewards
#* @return the rewards
#*/
     double[] getRewards():
       double[] rewards = new double[getStateCount()]
       for (int i = 0 i < rewards.length i++):
           rewards[i] = ((UnivariateGaussian) getOutputDistributions()[i]).getMean()
       }
       return rewards
    }
    
#/**
#* Get the reward for a state
#* @param state the state
#* @return the reward
#*/
     double reward(int state, int action):
        return ((UnivariateGaussian) getOutputDistributions()[state]).getMean()
    }
    
#/**
#* Set the transition matrices
#* @param matrices the matrices
#*/
      setTransitionMatrices(double[][][] matrices):
        StateDistribution[] transitions = new StateDistribution[matrices.length]
        for (int i = 0 i < matrices.length i++):
            transitions[i] = new SimpleStateDistributionTable(matrices[i])
        }
        setTransitionDistributions(transitions)
    }
    
#/**
#* Get the transition matrices
#* @return the transition matrices
#*/
     double[][][] getTransitionMatrices():
       double[][][] matrices = new double[getStateCount()][][]
       for (int i = 0 i < matrices.length i++):
           matrices[i] = ((SimpleStateDistributionTable) 
               getTransitionDistributions()[i]).getProbabilityMatrix()
       }
       return matrices
    }
    
#/**
#* Get the probability of transitioning from state i to state j,
#* with observation o
#* @param i the first state
#* @param j the second state
#* @param a the action
#* @return the probability
#*/
     double transitionProbability(int i, int j, int a):
        return ((SimpleStateDistributionTable) getTransitionDistributions()[i])
            .getProbabilityMatrix()[a][j]
    }
    
#/**
#* Sample a next state given the current state and input
#* @param i the current state
#* @param a the action
#* @return the next state
#*/
     int sampleState(int i, int a):
        return getTransitionDistributions()[i].generateRandomState(new Instance(a))
    }
    
#/**
#* Get the action count
#* @return the action count
#*/
     int getActionCount():
        return ((SimpleStateDistributionTable) 
            getTransitionDistributions()[0]).getInputRange()
    }
    
#/**
#* Set the initial state
#* @param i the new initial state
#*/
      setInitialState(int i):
        double[] p = new double[getStateCount()]
        p[i] = 1
        setInitialStateDistribution(new SimpleStateDistribution(p))
    }

#/**
#* @see rl.MarkovDecisionProcess#sampleInitialState()
#*/
     int sampleInitialState():
        return sampleInitialState(null)
    }

#/**
#* @see rl.MarkovDecisionProcess#isTerminalState(int)
#*/
     boolean isTerminalState(int state):
        return false
    }
}
